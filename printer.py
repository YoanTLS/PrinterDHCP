from scapy.all import *
from scapy.layers.dhcp import *
from scapy.layers.inet import UDP, IP
from scapy.layers.l2 import Ether


client_mac = "00:11:22:33:44:55"  
client_ip = "0.0.0.0"
server_ip = "255.255.255.255"


ethernet = Ether(dst="ff:ff:ff:ff:ff:ff", src=client_mac, type=0x0800)
ip = IP(src=client_ip, dst=server_ip)
udp = UDP(sport=68, dport=67)
bootp = BOOTP(chaddr=[mac2str(client_mac)], xid=RandInt(), flags=0x8000)
dhcp = DHCP(options=[
    ("message-type", "discover"),
    ("param_req_list", [1, 3, 6, 12, 15, 28, 42, 51, 54, 58, 59]),
    ("vendor_class_id", "Toshiba"),  # Toshiba for exemple
    ("client_identifier", client_mac),
    "end"
])

dhcp_discover = ethernet / ip / udp / bootp / dhcp

sendp(dhcp_discover, iface="eth0")
