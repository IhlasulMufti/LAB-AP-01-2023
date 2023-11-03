Harga = int(input("Masukkan Harga barang: "))
Pembayaran = int(input("Masukkan Uang Anda: "))
if Harga > Pembayaran:
    print("Uang tidak cukup")
else:
    Kembalian = Pembayaran - Harga
    seratus, limapuluh, duapuluh, sepuluh, limaribu, duaribu, seribu = 0, 0, 0, 0, 0, 0, 0
 
    while Kembalian > 0:
            if Kembalian >= 100000:
                seratus += 1
                Kembalian -= 100000
            elif Kembalian >= 50000:
                limapuluh += 1
                Kembalian -= 50000
            elif Kembalian >= 20000: 
                duapuluh += 1
                Kembalian -= 20000
            elif Kembalian >= 10000:
                sepuluh += 1
                Kembalian -= 10000
            elif Kembalian >= 5000:
                limaribu += 1
                Kembalian -= 5000
            elif Kembalian >= 2000:
                duaribu += 1
                Kembalian -= 2000
            elif Kembalian >= 1000:
                seribu += 1
                Kembalian -= 1000

            print(f"{seratus} uang Sejumlah RP 100.000")
            print(f"{limapuluh} uang Sejumlah RP 50.000")
            print(f"{duapuluh} uang Sejumlah RP 20.000")
            print(f"{sepuluh} uang Sejumlah RP 10.000")
            print(f"{limaribu} uang Sejumlah RP 5.000")
            print(f"{duaribu} uang Sejumlah RP 2.000")
            print(f"{seribu} uang Sejumlah RP 1.000")
