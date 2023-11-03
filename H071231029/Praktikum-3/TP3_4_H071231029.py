angka1=int(input("Masukkan bilangan pertama "))
hasil = angka1
while True:
    print("Pilihlah Bilangan Operasi yang ingin anda Masukkan\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\n5.Hasil ")
    menu =int(input(" = "))
    
    if menu == 5:
        print(hasil)
        break
    elif menu == 1 or menu == 2 or menu == 3 or menu == 4:
        angka2=int(input("Masukkan bilangan kedua "))
        if menu == 1:
            hasil += angka2
        elif menu == 2:
            hasil -= angka2
        elif menu == 3:
            hasil *= angka2
        elif menu == 4:
            hasil /= angka2
    else:
        print('Operasi tidak valid')
        break