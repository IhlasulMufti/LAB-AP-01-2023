awal = int(input("Masukan nilai :"))
print("-" *20)
while True:
    print("Menu:")
    print("1.Penjumlahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Pembagian")
    print("5.Hasil")
    
    menu= int(input("Pilih Menu:"))
    print("-" *20)
     
    if menu == 1:
         nilai = int(input("Masukan nilai:"))
         print("-" *20)
         awal += nilai
    elif menu == 2:
         nilai  = int(input("Masukan nilai:"))
         print("-" *20)
         awal -= nilai
    elif menu == 3:
         nilai = int(input("Masukan nilai:"))
         print("-" *20)
         awal *= nilai 
    elif menu == 4:
         nilai = int(input("Masukan nilai:"))
         print("-" *20)
         awal /= nilai 
    elif menu == 5:
         print(f"Hasil {awal}")
         break
    else:
         print("Menu Tidak Tersedia")
         print("-" *20)