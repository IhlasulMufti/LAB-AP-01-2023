
import re

def check_IP_address(input_text):
    ipv4_pattern = r'^(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$'

    if re.match(ipv4_pattern, input_text):
        return "IPv4"
    elif re.match(ipv6_pattern, input_text):
        return "IPv6"
    else:
        return "Bukan IP Address"

N = int(input("Masukkan jumlah baris input: "))
inputs = []

for _ in range(N):
    ip = input("Masukkan alamat IP: ")
    inputs.append(ip)

for ip in inputs:
    print(check_IP_address(ip))