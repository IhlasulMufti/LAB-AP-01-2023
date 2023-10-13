'''
def catAndMouse(catA, catB, mosC):
    # Hitung jarak antara kucing A dan tikus
    distA = abs(catA - mosC)

    # Hitung jarak antara kucing B dan tikus
    distB = abs(catB - mosC)

    if distA < distB:
        return "Cat A"
    elif distB < distA:
        return "Cat B"
    else:
        return "Mouse C"

# Test Case 1
print(catAndMouse(catA=16, catB=24, mosC=15))  # Output yang diharapkan: "Cat A"
print("Cat A")

# Test Case 2
print(catAndMouse(catA=20, catB=10, mosC=15))  # Output yang diharapkan: "Mouse C"
'''

''''''

'''
def catAndMouse(catA, catB, mosC):
    try:
        # Hitung jarak antara kucing A dan tikus
        jarakA = abs(catA - mosC)

        # Hitung jarak antara kucing B dan tikus
        jarakB = abs(catB - mosC)

        if jarakA < jarakB:
            return "Cat A"
        elif jarakB < jarakA:
            return "Cat B"
        else:
            return "Mouse C"

    except ValueError as e:
        return str(e)

try:
    # Meminta input dari pengguna
    catA = int(input("Masukkan posisi Kucing A: "))
    catB = int(input("Masukkan posisi Kucing B: "))
    mosC = int(input("Masukkan posisi Tikus C: "))

    # Memanggil fungsi catAndMouse dengan input pengguna
    hasil = catAndMouse(catA, catB, mosC)

    # Mencetak hasil
    print("Hasil:", hasil)
except Exception as e:
    print(f'Terjadi kesalahan karena {e}')
'''

def CatAndMouse(CatA, CatB, MosC):

    JarakA = abs(CatA - MosC)
    JarakB = abs(CatB - MosC)

    if JarakA < JarakB:
        return "Cat A"
    elif JarakB < JarakA:
        return "Cat B"
    else:
        return "Mouse C"
    
catA = int(input("Masukkan Posisi Kucing A: "))
catB = int(input("Masukkan Posisi Kucing B: "))
mosC = int(input("Masukkan Posisi Tikus C: "))

hasil = CatAndMouse(catA, catB, mosC)

print("Hasil:", hasil)