from scapy.all import ARP, Ether, srp
import sys
import requests

# Tarmoq interfeysini aniqlash (masalan: "eth0" yoki "wlan0")
interface = "wlp0s20f3"  # O'zingizning interfeysingizga moslashtiring
# Skanelayotgan tarmoq diapazoni (masalan, "192.168.1.0/24")
target_ip = "10.50.7.0/20"  # O'zingizning tarmoq diapazoningizga moslashtiring


def get_vendor(mac):
    """MAC manzil bo'yicha qurilma ishlab chiqaruvchisini aniqlash"""
    url = f"https://api.macvendors.com/{mac}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return "Noma'lum vendor"
    except:
        return "Internet ulanishi xatosi"


def scan_network(ip):
    try:
        # ARP so'rovini yaratish
        arp = ARP(pdst=ip)
        # Ethernet ramkasini yaratish (broadcast)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        # Paketni birlashtirish
        packet = ether / arp
        # Paketni yuborish va javoblarni qabul qilish
        result = srp(packet, timeout=3, iface=interface, verbose=False)[0]
        # Natijalarni saqlash uchun ro'yxat
        devices = []
        # Har bir javobni qayta ishlash
        for sent, received in result:
            vendor = get_vendor(received.hwsrc)  # Vendor aniqlash
            devices.append({'ip': received.psrc, 'mac': received.hwsrc, 'vendor': vendor})
        return devices
    except Exception as err:
        print(err)
        return []


def save_to_file(devices):
    # Faylga yozish
    with open("mac_addresses.txt", "w") as file:
        file.write("IP Address\t\tMAC Address\t\tVendor\n")
        file.write("-" * 60 + "\n")
        for device in devices:
            file.write(f"{device['ip']}\t\t{device['mac']}\t\t{device['vendor']}\n")


def main():
    print("Tarmoqni skanlash boshlandi...")
    devices = scan_network(target_ip)
    if devices:
        print(f"Topilgan qurilmalar soni: {len(devices)}")
        print("\nIP Address\t\tMAC Address\t\tVendor")
        print("-" * 60)
        for device in devices:
            print(f"{device['ip']}\t\t{device['mac']}\t\t{device['vendor']}")
        # Natijalarni faylga saqlash
        save_to_file(devices)
        print("\nNatijalar 'mac_addresses.txt' fayliga saqlandi!")
    else:
        print("Hech qanday qurilma topilmadi!")


if __name__ == "__main__":
    main()
