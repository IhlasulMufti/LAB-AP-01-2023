# #nomor 1 (segitiga)
print('Menghitung luas permukaan dan keliling segitiga')
x= float(input('Panjang sisi X= '))
y= float(input('Panjang sisi Y= '))

luas_segitiga=1/2*(x*y)
z= (x**2+y**2)**0.5
keliling= x+y+z

print(f'luas permukaan: {luas_segitiga: .2f}')
print(f'keliling: {keliling: .2f}')
