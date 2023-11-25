import re

def tentukan_jenis_ip(n, hasil,iterasi):

    if n == 0:
        return
    else:
        inputan = input("Masukkan inputan {} : ".format(iterasi)).strip() # strip untuk menghapus spasi di awal dan akhir string
        pola1 = r"^(\d{1,3}\.){3}\d{1,3}$"
        pola2 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

        ipv4 = re.match(pola1, inputan)
        ipv6 = re.match(pola2, inputan)

        if ipv4 and all(0 <= int(segment) <= 255 for segment in ipv4.group(0).split('.')):
            hasil.append("IPv4")
        elif ipv6:
            hasil.append("IPv6")
        else:
            hasil.append("Bukan IP Address")
        tentukan_jenis_ip(n - 1, hasil,iterasi+1)

n = int(input("N: "))
iterasi = 1
hasil2 = []

tentukan_jenis_ip(n, hasil2,iterasi)

for i in hasil2:
    print(i)