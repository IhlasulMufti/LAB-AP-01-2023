def hapusnol(ip_address):
    hapus0 = [str(int(i)) for i in ip_address]
    hasil= '.'.join(hapus0)
    return hasil
    

ip = input('Masukkan IP: ').split('.')
print(hapusnol(ip))



    



