nilai_a = float(input("Masukkan nilai : "))
while True:
    print('-'*20)
    print('Menu:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Nilai')
    operasi = int(input('Pilih Menu : '))
    print('-'*20)
    if operasi < 5:
        nilai_b = float(input('Masukkan Nilai : '))
    match operasi:
        case 1:
            nilai_a = nilai_a + nilai_b
        case 2:
            nilai_a = nilai_a - nilai_b
        case 3:
            nilai_a = nilai_a * nilai_b
        case 4:
            nilai_a = nilai_a / nilai_b
        case 5:
            print("{}".format(nilai_a))
            break
        case _:
            print('Operasi Tersebut Tidak ada!')

            
