n = int(input("Input berapa banyak suku yang ingin dijumlahkan: "))

a,b = 0,1

if n <= 1:
    print("0")

elif n == 1:
    print("0")

else:
    print("0", end=" ")
    for _ in range(1, n):
        a = b
        b = a + b
        print(a, end=" ")