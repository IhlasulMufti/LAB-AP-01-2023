print("Menghitung luas permukaan dan keliling segitiga")
x = float(input("Masukkan nilai x: "))
y = float(input("Masukkan nilai y: "))

# z = sisi miring 
z = (x ** 2 + y ** 2) ** 0.5
print(f"Sisi miring adalah: {z:.2f}") # Setelah titik ada 2 angka di belakangnya

# k = keliling segitiga
keliling_segitiga = x + y + z 
print("Keliling segitiga adalah: {:.1f}".format(keliling_segitiga))

# Luas segitiga
luas_segitiga = 0.5 * x * y
print(f"Luas segitiga adalah: {luas_segitiga:.2f}")