# fibonacci menggunakan fungsi rekursif
def fibonacci(suku_n,a,b):
    if(suku_n <= 0):
        return
    print(a, end=' ')  # Mencetak nilai a tanpa newline
    c = a
    a = b 
    b = c + b
    suku_n -= 1
    fibonacci(suku_n,a,b)

# suku = int(input("Masukkan Suku dari fibonacci : "))
while True:
    print("\n1. default\n2. Custom\n3. Exit")
    pilihan = int(input("Masukkan Pilihan : "))
    match pilihan:
        case 1:
            suku = int(input("Masukkan Suku : "))
            fibonacci(suku,0,1)
        case 2:
            suku = int(input("Masukkan Suku : "))
            angka1 = int(input("Masukkan Angka Pertama : "))
            angka2 = int(input("Masukkan Angka Kedua : "))
            fibonacci(suku,angka1,angka2)
        case 3:
            break
        case _:
            print("Menu Tidak Tersedia!")




