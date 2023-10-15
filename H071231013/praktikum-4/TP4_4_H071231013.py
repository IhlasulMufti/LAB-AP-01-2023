def catAndMouse(catA, catB, mosC):
    
    jarakA = abs(catA - mosC)

    jarakB = abs(catB - mosC)

    if jarakA < jarakB:
        return "Cat A"
    elif jarakB < jarakA:
        return "Cat B"
    else:
        return "Mouse C"   

catA = int(input("Masukkan posisi Kucing A: "))
catB = int(input("Masukkan posisi Kucing B: "))
mosC = int(input("Masukkan posisi Tikus C: "))

hasil = catAndMouse(catA, catB, mosC)

print("Hasil:", hasil)