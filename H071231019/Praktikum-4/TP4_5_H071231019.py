def fibonacci_rekursif(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci_rekursif(n - 1, b, a + b)
    
print("-------Welcome to Fibonacci Program-------")
while True:
    print("Menu: ")
    print("------------------------")
    print("1. Default Number")
    print("2. Custom Number")
    print("3. Exit")
    print("------------------------")
    pilihan = int(input("Choose your mode (1/2/3): "))
    print("------------------------")

    if pilihan == 1:
        jumlah_deret = int(input("Masukkan Jumlah Iterasi: "))
        hasil = [fibonacci_rekursif(i) for i in range(jumlah_deret)]
        print("Deret Fibonacci:", hasil)
        print("------------------------")

    elif pilihan == 2:
        jumlah_deret = int(input("Masukkan jumlah iterasi: "))
        nilai_awal1 = int(input("Masukkan Angka Pertama: "))
        nilai_awal2 = int(input("Masukkan Angka Kedua: "))
        hasil = [fibonacci_rekursif(i, nilai_awal1, nilai_awal2) for i in range(jumlah_deret)]
        print("Deret Fibonacci:", hasil)
        print("------------------------")

    elif pilihan == 3:
        print("Terima kasih, program telah selesai!")
        print("-----------------------------------")
        break

    elif pilihan not in [1, 2, 3] :
        print("Menu tidak tersedia")
        print("-------------------")