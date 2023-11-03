harga_barang = int(input("Masukan Harga Barang : "))
jumlah_uang = int(input("Jumlah Uang : "))
if jumlah_uang < harga_barang:
    print('Uang yang anda bayarkan kurang')
else:
    kembalian = jumlah_uang - harga_barang

    pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]

    for i in pecahan_uang:
        jumlah_pecahan = kembalian // i
        kembalian %= i
        print(f"{jumlah_pecahan} uang sejumlah Rp.{i}")
