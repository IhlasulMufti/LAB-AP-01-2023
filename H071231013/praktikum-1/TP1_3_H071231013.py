# Input a, b, dan c
a = float(input("Masukkan nilai a (a ≠ 0): "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

# Memastikan a tidak sama dengan 0
if a == 0:
    print("Nilai a tidak boleh sama dengan 0.")
else:
    # Menghitung diskriminan
    diskriminan = b**2 - 4*a*c

    # Menghitung solusi
    if diskriminan > 0:
        x1 = (-b + (diskriminan)**0.5) / (2*a)
        x2 = (-b - (diskriminan)**0.5) / (2*a)
        print(f"Solusi x1: {x1:.2f}")
        print(f"Solusi x2: {x2:.2f}")
    elif diskriminan == 0:
        x = -b / (2*a)
        print(f"Hanya ada satu solusi: x = {x:.2f}")
    else:
        realPart = -b / (2*a)
        imaginaryPart = (abs(diskriminan)**0.5) / (2*a)
        print(f"Solusi kompleks: x1 = {realPart:.2f} + {imaginaryPart:.2f}i")
        print(f"Solusi kompleks: x2 = {realPart:.2f} - {imaginaryPart:.2f}i")
