# Input sisi X dan Y
sisi_x = float(input("Masukkan panjang sisi X: "))
sisi_y = float(input("Masukkan panjang sisi Y: "))    

# Menghitung sisi Z (menggunakan rumus Pythagoras)
sisi_z = (sisi_x ** 2 + sisi_y ** 2) ** 0.5

# Menghitung keliling segitiga (sisi X + sisi Y + sisi Z)
keliling = sisi_x + sisi_y + sisi_z

# Menghitung luas segitiga (0.5 * sisi X * sisi Y)
luas = 0.5 * sisi_x * sisi_y

# Menampilkan hasil dengan dua angka di belakang koma
print(f"Luas Segitiga XYZ: {luas:.5f}")
print(f"Keliling Segitiga XYZ: {keliling:.3f}")