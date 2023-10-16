def hilang_nol(ipadd):
    ip_baru=[]
    ip_add= ipadd.split(".")
    for ip in ip_add:
        ipd=str(int(ip))
        ip_baru.append(ipd)
    ip_baru= ".".join(ip_baru)
    return ip_baru
ipadd= input()
print(hilang_nol(ipadd))