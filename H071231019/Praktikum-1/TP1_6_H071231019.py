print("Rumus belah ketupat")

s = float(input("Masukkan sisi 1: "))
d1 = float(input("Masukkan diagonal 1: "))
d2 = float(input("Masukkan diagonal 2: "))

luas = 0.5 * d1 * d2
keliling = 4 * s

print("Luas belah ketupat: {:.2f}".format(luas))
print("Keliling belah ketupat: {:.2f}".format(keliling))