print("MENGHITUNG LUAS PERMUKAAN DAN KELILING SEGITIGA")
print("By A.M.Yusran Mazidan")
x = float(input("Panjang sisi X : "))
y = float(input("Panjang sisi Y : "))

luas = ( x * y ) / 2
SisiMiring = (x**2 + y**2)**(1/2)
keliling = x + y + SisiMiring

print(f"Luas Permukaan : {round(luas,2)}")
print(f"Keliling : {round(keliling,2)}")
