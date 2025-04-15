import pyshark
import collections
import time
import os
import msvcrt  # Windows-compatible keypress detection
import sys

# Dictionary to store IP counts
ip_counter = collections.Counter()
INITIAL_ATTACK_THRESHOLD = 10
INCREASED_ATTACK_THRESHOLD = 100
attack_threshold = INITIAL_ATTACK_THRESHOLD  # Dynamic threshold

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def loading_screen():
    """Creates a cool loading animation when the program starts."""
    os.system("cls" if os.name == "nt" else "clear")
    print(CYAN + "\n🌐 Initializing Real-Time Network Monitor..." + RESET)
    animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", 
                 "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", 
                 "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", 
                 "[■■■■■■■■■■] 100% 🚀 Ready!"]

    for frame in animation:
        sys.stdout.write("\r" + CYAN + frame + RESET)
        sys.stdout.flush()
        time.sleep(0.3)
    
    print("\n" + GREEN + "✅ System Initialized! Starting Network Monitoring...\n" + RESET)
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")  # Clear screen after loading

def print_banner():
    """Fancy banner for network monitoring"""
    print(GREEN + "=" * 80)
    print(" 🚀 Real-Time Packet Logging & DDoS Detection 🌐 ")
    print("=" * 80 + RESET)

def check_keypress():
    """Check if a key has been pressed to reset threshold"""
    if msvcrt.kbhit():
        msvcrt.getch()  # Consume the keypress
        return True
    return False

def detect_ddos():
    global attack_threshold
    capture = pyshark.LiveCapture(interface="Wi-Fi")  # Ensure correct network interface
    loading_screen()  # Show the loading animation before starting
    print_banner()
    print(GREEN + "📡 Monitoring network traffic... checking for malicious packets\n" + RESET)

    packet_count = 0  # Counter for packets logged
    threshold_reset = False  # Track if threshold has been reset

    try:
        for packet in capture.sniff_continuously():
            try:
                packet_count += 1  # Increment packet count
                log_entry = f" Packet logged number : {packet_count} - Size: {packet.length} bytes"

                attacker_ip = None  # Store attacker IP

                if "IP" in packet:
                    src_ip = packet.ip.src
                    dst_ip = packet.ip.dst
                    protocol = packet.transport_layer if hasattr(packet, "transport_layer") else "Unknown"
                    log_entry += f" | {protocol} | {src_ip} ➝ {dst_ip}"

                    # Count IP occurrences
                    ip_counter[src_ip] += 1

                    # Store potential attacker IP
                    if len(ip_counter) > attack_threshold:
                        attacker_ip = src_ip  

                # Check if key is pressed to reset the IP count
                if check_keypress():
                    ip_counter.clear()  # Reset detection
                    attack_threshold = INCREASED_ATTACK_THRESHOLD  # Increase threshold after first reset
                    time.sleep(2)

                # Check attack status
                unique_ips = len(ip_counter)
                if unique_ips > attack_threshold:
                    status_message = RED + "🔥 UNDER ATTACK! ❌" + RESET
                    attacker_line = YELLOW + f"⚠️ Attacker IP Address: {attacker_ip}, Attack type : 7" + RESET if attacker_ip else ""
                else:
                    status_message = GREEN + "🛡️ SYSTEM SAFE ✅" + RESET
                    attacker_line = ""

                # Print new packet log
                print(f"{status_message}\n{GREEN if unique_ips <= attack_threshold else RED}{log_entry}{RESET}")
                if attacker_line:
                    print(attacker_line)  # Show attacker IP in yellow only during attack

                time.sleep(0.1)  # Smooth output updates

            except AttributeError:
                continue  # Ignore packets without an IP layer

    except KeyboardInterrupt:
        print(GREEN + "\n👋 Exiting Network Monitoring... Stay Safe! 🔒" + RESET)

if __name__ == "__main__":
    detect_ddos()
