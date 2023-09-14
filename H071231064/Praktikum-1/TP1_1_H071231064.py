print("MENGHITUNG LUAS PERMUKAAN DAN KELILING SEGITIGA")
print("By A.M.Yusran Mazidan")
x = float(input("Panjang sisi X : "))
y = float(input("Panjang sisi Y : "))

luas = ( x * y ) / 2
SisiMiring = (x**2 + y**2)**(1/2)
keliling = x + y + SisiMiring

print("Luas Permukaan : {:.2f}".format(luas))
print("Keliling Permukaan : {:.2f}".format(keliling))
