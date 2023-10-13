print('Kalkulator Sederhana \n------------------------')
awal = float(input('Masukkan nilai awal= '))

while True:
    print("-------------------------")
    print('Menu \n 1.Penjumlahan \n 2.Pengurangan \n 3.Perkalian \n 4.Pembagian \n 5.Hasil')
    menu = int(input('Pilih Menu= '))
    if menu == 1:
        akhir = float(input('Masukkan nilai= '))
        awal += akhir
    elif menu == 2:
        akhir = float(input('Masukkan nilai= '))
        awal -= akhir
    elif menu == 3:
        akhir = float(input('Masukkan nilai= '))
        awal *= akhir
    elif menu == 4:
        akhir = float(input('Masukkan nilai= '))
        awal /= akhir
    elif menu == 5:
        print(f'Hasilnya adalah {awal}')
        break
    else:
        print('Menu Tidak Tersedia')
