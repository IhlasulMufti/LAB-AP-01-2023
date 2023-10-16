ip = input('Masukkan IP: ')
ip= ip.split('.')

hapus0 = [str(int(i)) for i in ip]

hasil = '.'.join(hapus0)

print(hasil)


    



