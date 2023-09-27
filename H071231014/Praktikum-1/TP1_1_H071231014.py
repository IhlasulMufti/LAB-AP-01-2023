x = float(input('masukan nilai x :')) 
y = float(input('masukan nilai y :')) 

z = (x**2+y**2)**0.5  

luas = 0.5*x*y

keliling = x+y+z 
 
print('luas = {:.2f}'.format(luas))
print('keliling = {:.2f}'.format(keliling))