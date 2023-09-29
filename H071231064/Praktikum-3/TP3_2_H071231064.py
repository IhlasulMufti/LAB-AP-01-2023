harga_barang = int(input("Masukkan Harga Barang : "))
nilai_uang = int(input("Masukkan Nilai Uang : "))
pecahan_uang = [[100000,0],[50000,0],[20000,0],[10000,0],[5000,0],[2000,0],[1000,0]]

kembalian = nilai_uang - harga_barang
if kembalian < 0 :
    print("Mohon Maaf uangnya kurang")
    quit()
elif kembalian == 0 :
    print("Uangnya pas")
    quit()
else:
    # menghitung kembalian dengan cara mengurangi kembalian dari pecahan terbesar, jika tidak dapat dikurangi dengan pecahan besar maka akan dikurangi ke pecahan dibawahnya
    for pecahan in pecahan_uang:
        while kembalian >= pecahan[0]:
            kembalian -= pecahan[0]
            pecahan[1] += 1
    # print sesuai dengan list / array yang telah dibuat
    for pecahan in pecahan_uang:
        print("{} uang sejumlah Rp.{}".format(pecahan[1],pecahan[0]))

        