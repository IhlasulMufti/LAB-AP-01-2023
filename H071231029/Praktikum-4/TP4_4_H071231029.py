def catAndMouse(catA,catB, MosC):
    jarak_kucing_A = abs(catA-MosC)
    jarak_kucing_B = abs(catB-MosC)

    if jarak_kucing_B < jarak_kucing_A:
        print("Maka Kucing B menang")
    elif jarak_kucing_B > jarak_kucing_A:
        print("Maka kucing A menang")
    else:
        print("Kedua kucing betemu dan Tikus lolos") 


catA = int(input("Masukkan Posisi Kucing A "))
catB = int(input("Masukkan Posisi Kucing B "))
MosC = int(input("Masukkan Posisi Tikus "))
(catAndMouse(catA,catB,MosC))