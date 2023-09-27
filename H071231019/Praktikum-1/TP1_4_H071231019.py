print("Pengujian jenis karakter\n------------------------")
x = input("Masukkan sebuah karakter: ")

kapital = x >= 'A' and x <= 'Z'
kecil = x >= 'a' and x <= 'z'
angka = x >= '0' and x <= 'z'

print(f"Huruf Kapital? {kapital}")
print(f"Huruf Kecil? {kecil}")
print("Angka? {}".format(angka))