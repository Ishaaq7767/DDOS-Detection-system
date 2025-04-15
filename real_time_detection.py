import pyshark
import time
import sys
from collections import defaultdict
from colorama import Fore, Style, init
import threading

# Initialize colorama
init(autoreset=True)

def animate():
    """ Creates a rotating animation while monitoring """
    while True:
        for char in "|/-\\":
            sys.stdout.write(f"\r{Fore.CYAN}Monitoring network... {char}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)

def detect_ddos(interface='Wi-Fi'):
    print(f"{Fore.GREEN}🚀 Real-Time DDoS Attack Detection Started on {interface}!{Style.RESET_ALL}")
    print("=" * 60)
    capture = pyshark.LiveCapture(interface=interface)
    ip_packet_count = defaultdict(int)
    alert_threshold = 100  # Adjust as needed

    threading.Thread(target=animate, daemon=True).start()

    try:
        for packet in capture.sniff_continuously():
            if 'IP' in packet:
                src_ip = packet.ip.src
                ip_packet_count[src_ip] += 1
                
                # Normal Monitoring Message
                sys.stdout.write(f"\r{Fore.GREEN}✅ Safe: Normal traffic detected ({len(ip_packet_count)} active IPs)...")
                sys.stdout.flush()
                
                if ip_packet_count[src_ip] > alert_threshold:
                    print(f"\n{Fore.RED}⚠️  [ALERT] Potential DDoS Attack Detected! ⚠️")
                    print(f"   🚨 Suspicious IP: {Fore.YELLOW}{src_ip}{Style.RESET_ALL} ")
                    print(f"   📊 Packets Received: {Fore.YELLOW}{ip_packet_count[src_ip]}{Style.RESET_ALL} ")
                    print(f"   ⏳ Time: {Fore.YELLOW}{time.strftime('%H:%M:%S')}{Style.RESET_ALL}")
                    print("=" * 60)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}🛑 Monitoring stopped by user.{Style.RESET_ALL}")

if __name__ == "__main__":
    detect_ddos()
