import re

def cek_IPaddress(address):
    IPv4_Address = r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\." \
                    r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\." \
                    r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\." \
                    r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
    IPv6_Address = r"^(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}$"
    if re.match(IPv4_Address, address):
        return "IPv4"
    elif re.match(IPv6_Address, address):
        return "IPv6"
    else:
        return "Bukan IP Address"

address = input("Masukkan alamat IP: ")
hasil = cek_IPaddress(address)
print(hasil)