#nomor 5
print('Konversi Detik ke Jam')
a= int(input('Masukkan Jumlah Detik= '))

jam = a//3600
sisa= a%3600
menit= sisa//60
detik= sisa%60

print('{:02}:{:02}:{:02}'.format(jam,menit,detik))