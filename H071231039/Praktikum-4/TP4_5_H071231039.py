def fibonacci(angka,a=0,b=1):
   if angka > 0:
        print(a, end= " ")
        c = a+b
        a = b
        b = c
        fibonacci(angka-1,a,b)


print('='*40)
print('Selamat datang di program fibonacci')
print('='*40)

while True:
    print('\nSilahkan pilih menu\n1.Default Number\n2.Custom Number\n3.Exit')
    menu = int(input('\n= '))
    if menu == 1:
        menu1 = int(input('Masukkan angka= '))
        fibonacci(menu1)

    elif menu == 2:
        iterasi= int(input('Masukkan iterasi= '))
        angkasatu= int(input('Masukkan angka pertama= '))
        angkadua= int(input('Masukkan angka kedua= '))
        fibonacci(iterasi,angkasatu,angkadua)

    elif menu == 3:
        print('Terima Kasih')
        exit()

    else:
        print('Menu tidak tersedia')