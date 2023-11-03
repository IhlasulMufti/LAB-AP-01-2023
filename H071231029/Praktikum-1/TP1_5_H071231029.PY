print(f'Konversi detik ke jam')
s = int(input(f'Masukkan jumlah detik: '))
jam = s // 3600
sisa_s = s % 3600
menit = sisa_s // 60
detik = sisa_s % 60
print(f'{jam:02}:{menit:03}:{detik:04}')