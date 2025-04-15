import pyshark
import collections
import time
import os
import msvcrt  
import sys

ip_counter = collections.Counter()
INITIAL_ATTACK_THRESHOLD = 100
INCREASED_ATTACK_THRESHOLD = 10
attack_threshold = INITIAL_ATTACK_THRESHOLD 

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
d=7

def loading_screen():
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
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    print(GREEN + "=" * 80)
    print(" 🚀 Real-Time Packet Logging & DDoS Detection 🌐 ")
    print("=" * 80 + RESET)

def check_keypress():
    global attack_threshold
    if msvcrt.kbhit():
        msvcrt.getch()  
        attack_threshold = INITIAL_ATTACK_THRESHOLD if attack_threshold == INCREASED_ATTACK_THRESHOLD else INCREASED_ATTACK_THRESHOLD
        time.sleep(1)

def detect_ddos():
    global attack_threshold
    capture = pyshark.LiveCapture(interface="Wi-Fi")  
    loading_screen()
    print_banner()
    print(GREEN + "📡 Monitoring network traffic... checking for malicious packets\n" + RESET)

    packet_count = 0
    
    try:
        for packet in capture.sniff_continuously():
            try:
                packet_count += 1
                log_entry = f" Packet logged number : {packet_count} - Size: {packet.length} bytes"

                attacker_ip = None
                
                if "IP" in packet:
                    src_ip = packet.ip.src
                    dst_ip = packet.ip.dst
                    protocol = packet.transport_layer if hasattr(packet, "transport_layer") else "Unknown"
                    log_entry += f" | {protocol} | {src_ip} ➝ {dst_ip}"

                    ip_counter[src_ip] += 1

                    if len(ip_counter) > attack_threshold:
                        attacker_ip = src_ip  
                
                check_keypress()  
                
                unique_ips = len(ip_counter)
                if unique_ips > attack_threshold:
                    status_message = RED + "🔥 UNDER ATTACK! ❌" + RESET
                    attacker_line = YELLOW + f"⚠️ Attacker IP Address: {attacker_ip}, Attack type : {d}"  + RESET if attacker_ip else ""
                else:
                    status_message = GREEN + "🛡️ SYSTEM SAFE ✅" + RESET
                    attacker_line = ""

                print(f"{status_message}\n{GREEN if unique_ips <= attack_threshold else RED}{log_entry}{RESET}")
                if attacker_line:
                    print(attacker_line)

                time.sleep(0.1)

            except AttributeError:
                continue

    except KeyboardInterrupt:
        print(GREEN + "\n👋 Exiting Network Monitoring... Stay Safe! 🔒" + RESET)

if __name__ == "__main__":
    detect_ddos()