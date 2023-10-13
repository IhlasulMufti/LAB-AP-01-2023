def angka_terbesar(daftar_angka):
    angka_terbesar = daftar_angka[0]
    for angka in daftar_angka:
        if angka > angka_terbesar:
            angka_terbesar = angka
    return angka_terbesar

print("Uji Angka")
while True:
    daftar_angka = int(input("Jumlah item = "))
    nomor = []
    for i in range(daftar_angka):
        y = int(input("Angka = "))
        nomor.append(y)
    print(f'Angka terbesar adalah {angka_terbesar(nomor)}')
    break