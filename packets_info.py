import pyshark

# Set the interface to Wi-Fi explicitly
INTERFACE = "Wi-Fi"

def detect_ddos():
    print(f"Monitoring network for DDoS attacks on interface: {INTERFACE}...")

    try:
        capture = pyshark.LiveCapture(interface=INTERFACE)
        for packet in capture.sniff_continuously(packet_count=10):
            print(f"Captured packet: {packet}")
    except Exception as e:
        print(f"Error capturing packets: {e}")

# Run detection
detect_ddos()
