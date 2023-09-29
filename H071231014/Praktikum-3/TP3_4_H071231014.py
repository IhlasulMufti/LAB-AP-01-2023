

awal = int(input("masukan nilai :"))
while True:
    print("menu:")
    print("1.Penjumlahan")
    print("2.Pengurangan")
    print("3.perkalian")
    print("4.Pembagian")
    print("5.Hasil")
    
    menu= int(input("pilih menu:"))
     
    if menu == 1:
         nilai = int(input("masukan nilai:"))
         awal += nilai
    elif menu == 2:
         nilai  = int(input("masukan nilai:"))
         awal -= nilai
    elif menu == 3:
         nilai = int(input("masukan nilai:"))
         awal *= nilai 
    elif menu == 4:
         nilai = int(input("masukan nilai:"))
         awal /= nilai 
    elif menu == 5:
         print(f"hasil {awal}")
         break
    else:
         print("menu tidak tersedia")
         

                   

