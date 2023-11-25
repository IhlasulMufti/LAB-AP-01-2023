angka_input = input("Masukkan beberapa angka (pisahkan dengan spasi): ")
angka_list = angka_input.split()

angka_genap = []
angka_ganjil = []
angka_habis_dibagi_5 = []

for angka in angka_list:
    angka = int(angka)
    if angka % 2 == 0:
        angka_genap.append(angka)
    else:
        angka_ganjil.append(angka)
    if angka % 5 == 0:
        angka_habis_dibagi_5.append(angka)

print(f"Angka Genap : {angka_genap}\nAngka Ganjil : {angka_ganjil}\nAngka yang habis dibagi 5 : {angka_habis_dibagi_5}")