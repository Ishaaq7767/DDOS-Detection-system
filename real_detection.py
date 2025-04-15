import pyshark
import time
import collections
import os

# Choose network interface (update if needed)
INTERFACE = "Wi-Fi"

# Detection parameters
THRESHOLD = 100  # Packets per second before flagging as an attack
TIME_WINDOW = 5  # Time window in seconds

# Track packet counts per IP
packet_counts = collections.defaultdict(int)

# Clear terminal function
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# Function to monitor network traffic
def detect_ddos():
    capture = pyshark.LiveCapture(interface=INTERFACE, display_filter="ip")

    print("\033[1;34m[INFO] Monitoring network for DDoS attacks...\033[0m\n")
    
    start_time = time.time()
    
    for packet in capture.sniff_continuously():
        try:
            ip_src = packet.ip.src
            packet_counts[ip_src] += 1
        except AttributeError:
            continue

        # Check time window
        if time.time() - start_time >= TIME_WINDOW:
            clear_terminal()
            print("\033[1;34m[INFO] Monitoring network for DDoS attacks...\033[0m\n")

            for ip, count in list(packet_counts.items()):
                packets_per_sec = count / TIME_WINDOW

                if packets_per_sec > THRESHOLD:
                    print(f"\033[1;31m⚠️ [ALERT] Potential DDoS Attack! Suspicious IP: {ip} (Packets/sec: {packets_per_sec:.2f})\033[0m")
                else:
                    print(f"\033[1;32m✔ [SAFE] Normal Traffic from {ip} (Packets/sec: {packets_per_sec:.2f})\033[0m")

            # Reset tracking
            packet_counts.clear()
            start_time = time.time()

# Run detection
detect_ddos()
