import pyshark

interfaces = pyshark.tshark.tshark.get_tshark_interfaces()
print("Available Interfaces:", interfaces)
