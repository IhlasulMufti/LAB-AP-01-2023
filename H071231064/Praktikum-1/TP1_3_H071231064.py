print("PERMASALAHAN SI KELVIN")
print("By A.M.Yusran Mazidan")
print("========================")

a = float(input("Input a = "))
b = float(input("Input b = "))
c = float(input("Input c = "))

# d adalah diskriminan
d = (b**2) - (4*a*c)

if d > 0 :
    x1 = (-b + d**(1/2)) / (2*a)
    x2 = (-b - d**(1/2)) / (2*a)
    print(f"x1 = {round(float(x1),2)}")
    print(f"x2 = {round(float(x2),2)}")
elif d == 0 :
    x = -b / (2*a)
    print(f"x = {x}")
else :
    print("tidak ada akar nyata dalam persamaan ini")



