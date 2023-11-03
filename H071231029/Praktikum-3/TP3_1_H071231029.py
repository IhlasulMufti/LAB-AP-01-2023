data = int(input("Masukkan Suku Fibonacci: "))
n1 = 0
n2 = 1

for i in range (data):
        print(n1, end = ' ')
        total = n1 + n2 
        n1 = n2
        n2 = total 

             