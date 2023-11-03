# Menerima input dari pengguna
inputan = input("Masukkan karakter atau angka: ")

# Inisialisasi variabel-variabel pengecekan
is_huruf_kapital = False
is_huruf_kecil = False
is_angka = False

# Memeriksa setiap karakter dalam inputan
for karakter in inputan:
    if karakter.isupper():
        is_huruf_kapital = True
    elif karakter.islower():
        is_huruf_kecil = True
    elif karakter.isdigit():
        is_angka = True

# Menampilkan hasil pengecekan
print(f'Huruf kapital: {is_huruf_kapital}')
print(f'Huruf kecil: {is_huruf_kecil}')
print(f'Angka: {is_angka}')
