#nomor 3
a= float(input('Input a = '))
if a==0:
    print('Inputan Tidak Valid')
    exit()
b= float(input('Input b = '))
c= float(input('Input c = '))

x1= (-b+(b**2-4*a*c)**0.5) / (2*a)
x2= (-b-(b**2-4*a*c)**0.5) / (2*a)

print('x1= {:.2f}'.format(x1))
print(f'x2= {x2: .2f}')
