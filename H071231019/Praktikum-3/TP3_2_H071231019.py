harga_barang = int(input("Masukkan Harga Barang : "))
jumlah_uang = int(input("Jumlah Uang : "))

kembalian = jumlah_uang - harga_barang

pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]

if jumlah_uang < harga_barang :
    print("Uang tidak cukup")
else : 
    for pecahan in pecahan_uang:
        jumlah_pecahan = kembalian // pecahan
        kembalian = kembalian % pecahan
        print(f"{jumlah_pecahan} uang sejumlah Rp.{pecahan}") 