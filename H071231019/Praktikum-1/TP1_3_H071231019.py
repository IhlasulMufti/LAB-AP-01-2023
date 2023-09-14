a = float(input("Nilai a adalah: "))
b = float(input("Nilai b adalah: "))
c = float(input("Nilai c adalah: "))


x1 = (-b + (b**2 - 4*a*c)**0.5) / 2*a
x2 = (-b - (b**2 - 4*a*c)**0.5) / 2*a
print(f"x1 adalah: {x1:.2f}")
print("x2 adalah: {:.2f}".format(x2))