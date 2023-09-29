print("Konversi detik ke jam")
d = int(input("Masukkan jumlah detik: "))

m = d // 60 #hasil pembagian bulat d dan 60 dimasukkan ke variabel m
sisa_detik = d % 60
j = m // 60 #hasil pembagian bulat m dan 60 dimasukkan ke variabel j
sisa_menit = m % 60

print("{:02}:{:02}:{:02}".format(j,sisa_menit,sisa_detik))