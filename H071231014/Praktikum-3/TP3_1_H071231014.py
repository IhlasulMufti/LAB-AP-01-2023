n = int(input())

x=0
y=1

for i in range(n):
    print(x, end=" ")
    z = x + y
    x = y
    y = z
   