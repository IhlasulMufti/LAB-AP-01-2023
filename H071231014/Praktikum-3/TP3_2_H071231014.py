harga_barang = int(input("Masukan Harga Barang : "))
jumlah_uang = int(input("Jumlah Uang : "))

kembalian = jumlah_uang - harga_barang

pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]

for pecahan in pecahan_uang:
    if jumlah_uang <  harga_barang :
        print("uang anda tidak cukup")
        break
    else :
        jumlah_pecahan = kembalian // pecahan
        kembalian %= pecahan
        print(f"{jumlah_pecahan} uang sejumlah Rp.{pecahan}")
    



     