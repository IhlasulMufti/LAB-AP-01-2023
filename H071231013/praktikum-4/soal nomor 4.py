def catAndMouse(catA, catB, mosC):
    # Hitung jarak antara kucing A dan tikus
    jarakA = abs(catA - mosC) # fungsi abs: jika nilainya negatif,tetap akan bernilai positif, contohnya: x = -100,print(abs(x))

    # Hitung jarak antara kucing B dan tikus
    jarakB = abs(catB - mosC)

    if jarakA < jarakB:
        return "Cat A" # fungsi return: mengembalikan nilai dari "cat a"
    elif jarakB < jarakA:
        return "Cat B"
    else:
        return "Mouse C"   

catA = int(input("Masukkan posisi Kucing A: "))
catB = int(input("Masukkan posisi Kucing B: "))
mosC = int(input("Masukkan posisi Tikus C: "))

# Memanggil fungsi catAndMouse dengan input pengguna
hasil = catAndMouse(catA, catB, mosC)

# Mencetak hasil
print("Hasil:", hasil)