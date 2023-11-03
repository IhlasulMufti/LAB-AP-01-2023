print('rumus lingkaran')
r= float(input('Masukkan jari jari= '))

if r%7==0:
    phi=22/7
else:
    phi=3.1415

luas= phi*(r**2) 
keliling= phi*2*r

print('Luas= {:.2f}'.format(luas))
print('Keliling= {:.2f}'.format(keliling))



