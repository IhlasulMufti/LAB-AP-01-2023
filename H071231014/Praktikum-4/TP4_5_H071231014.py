def fibonacci(angka, n1=0, n2=1,suku=0):
    print(n1, end=' ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    suku +=1
    if suku < angka:
        fibonacci(angka, n1, n2,suku)
print("\n-------Welcome To Fibonacci Program-------")
while True: 
    print("\n------------------------------\nChoose Your Mode")
    print("1.Default Number")
    print("2.Costum Number")
    print("3.Exit")
    pilihan= int(input("Pilih (1|2|3) :"))
    match pilihan:
        case 1:
            print("-"*30)    
            angka = int(input("Masukkan Jumlah iterasi: "))
            print("-"*30)
            fibonacci(angka)
        case 2:
            print("-"*30)
            angka = int(input("Masukkan Jumlah iterasi: "))
            print("-"*30)
            n1 = int(input("Masukkan Angka Pertama: "))
            n2 = int(input("Masukkan Angka Kedua: "))
            print("-"*30)
            fibonacci(angka, n1, n2)
        case 3:
            print("-"*30)
            print("Program selesai")
            print("-"*30)
            break
        case _:
            print("-"*30)
            print("Menu Tidak Tersedia")
            print("-"*30)
