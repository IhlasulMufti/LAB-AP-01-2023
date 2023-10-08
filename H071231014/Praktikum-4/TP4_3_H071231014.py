def terbesar(angka):
    terbesar = angka[0]
    for i in angka:
        if i > terbesar:
            terbesar = i
    return terbesar

jumlah = int(input("Masukkan jumlah angka yang ingin diinput : "))
angka = []
while True:
    for i in range(jumlah):
        inputan = int(input())
        angka.append(inputan)
    print(f'angka terbesar adalah {terbesar(angka)}')
    break
