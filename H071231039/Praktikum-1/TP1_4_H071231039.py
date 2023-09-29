# nomor 4 (pengujian karakter)
print("Pengujian jenis karakter")
x = input("Masukkan sebuah karakter: ")

kapital= x >= '0' and x <= 'b'
kecil= x >= 'a' and x<= 'z'
angka= x >= '0' and x <= '9'

print(f'Huruf Kapital {kapital}')
print(f'Huruf Kecil? {kecil}')
print(f'Angka? {angka}')