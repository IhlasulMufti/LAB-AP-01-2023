import re 

def IPv4(check):
    pola = r"^((\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])$"
    return re.search(pola, check)

def IPv6(check):
    pola = r"^([\da-fA-F]{0,4}:){7}[\da-fA-F]{0,4}$"
    return re.search(pola, check)

perulangan = int(input("banyak inputan : "))

var = []
for i in range(perulangan):
    var.append(input(f"input ke {i + 1} : "))

for i in var:
    if IPv4(i):
        print("IPv4")
    elif IPv6(i):
        print("IPv6")
    else:
        print("Bukan IP Adress")
