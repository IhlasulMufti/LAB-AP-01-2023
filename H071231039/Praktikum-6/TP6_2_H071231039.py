input_angka = input("Masukkan beberapa angka: ").split(' ')

angka = [int(x) for x in input_angka]


angka_genap = []
angka_ganjil = []
angka_habis_dibagi_5 = []

for i in angka:
    if i % 2 == 0:
        angka_genap.append(i)
    else:
        angka_ganjil.append(i)
    if i % 5 == 0:
        angka_habis_dibagi_5.append(i)


print("Angka Genap:", angka_genap)
print("Angka Ganjil:", angka_ganjil)
print("Angka yang habis dibagi 5:", angka_habis_dibagi_5)
