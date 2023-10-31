def isgenap(angka):
    return angka % 2 == 0

def isganjil(angka):
    return angka % 2 != 0

def iskelipatan5(angka):
    return angka % 5 == 0

angka = list(map(int,input("Masukkan beberapa angka: ").split()))

angka_genap = []
angka_ganjil = []
angka_yang_habis_dibagi_5 = []

for i in angka: 
    if isgenap(i):
        angka_genap.append(i)
    if isganjil(i):
        angka_ganjil.append(i)
    if iskelipatan5(i):
        angka_yang_habis_dibagi_5.append(i)

print("Angka Ganjil: ", angka_ganjil)
print("Angka Genap: ", angka_genap)
print("Angka yang habis dibagi 5: ", angka_yang_habis_dibagi_5)