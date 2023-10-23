daftar_angka = list(map(int, input("Masukkan angka : ").split()))

pasangan = []
angka1 = []
jumlah = 0

for angka in daftar_angka:
    if daftar_angka.count(angka) and angka not in pasangan:
        pasangan.append(angka)
        angka1.append(daftar_angka.count(angka))

for i in angka1:
    jumlah += (i//2)

print(f"{jumlah} pasangan")


