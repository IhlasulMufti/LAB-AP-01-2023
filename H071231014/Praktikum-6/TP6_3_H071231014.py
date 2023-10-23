def angka(input_angka):
    list_angka = list(map(int, input_angka.split()))
    genap = []
    ganjil = []
    habis5 = []

    for i in list_angka:
        if i % 2 == 0 :
            genap.append(i)
        if i % 2 != 0:
            ganjil.append(i)
        if i % 5 == 0:
            habis5.append(i)

    return genap, ganjil, habis5

input_angka = input("Masukkan beberapa angka: ")
genap, ganjil, habis5 = angka(input_angka)
print("Angka genap:", genap)
print("Angka ganjil:", ganjil)
print("Angka yang habis dibagi 5:", habis5)