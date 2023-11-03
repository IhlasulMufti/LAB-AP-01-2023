n = int(input("n: "))

x,y = 0,1

for i in range(n):
    print(x, end=" ")
    z = x + y
    x = y
    y = z 