bilangan1 = float(input("Masukkan Nilai 1: "))
while True:
    print("Menu: ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Hasil")

    pilihan = int(input("Pilih operasi (1/2/3/4/5): "))
    print("--------------------")

    if pilihan == 5:
        print("Hasil operasi dari {}".format(bilangan1))
        break

    if pilihan not in [1, 2, 3, 4]:
        print("Pilihan tidak valid.")
        print("--------------------")
        continue

    bilangan2 = float(input("Masukkan Nilai 2: "))
    print("--------------------")

    if pilihan == 1:
        bilangan1 += bilangan2
    elif pilihan == 2:
        bilangan1 -= bilangan2
    elif pilihan == 3:
        bilangan1 *= bilangan2
    elif pilihan == 4:
        bilangan1 /= bilangan2
        if bilangan2 == 0:
            print("Pembagian dengan 0 tidak diperbolehkan.")