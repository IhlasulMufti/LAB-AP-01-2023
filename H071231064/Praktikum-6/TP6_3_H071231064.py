def is_genap(angka):
    return angka % 2 == 0

def is_ganjil(angka):
    return angka % 2 != 0

def is_kelipatan_lima(angka):
    return angka % 5 == 0

angka = input("Masukkan beberapa angka dengan spasi: ").split()
angka = [int(item) for item in angka]

genap = [item for item in angka if is_genap(item)]
ganjil = [item for item in angka if is_ganjil(item)]
lima = [item for item in angka if is_kelipatan_lima(item)]

genap.sort()
ganjil.sort()
lima.sort()

print(f"Angka genap: {genap}\nAngka ganjil: {ganjil}\nAngka yang habis dibagi 5: {lima}")



