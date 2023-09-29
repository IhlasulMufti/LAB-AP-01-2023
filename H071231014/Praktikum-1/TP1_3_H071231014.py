a = float(input('nilai a ='))
b = float(input('nilai b ='))
c = float(input('nilai c ='))

x1 = (-b+ (b**2-4*a*c)**0.5)/(2*a)
x2 = (-b- (b**2-4*a*c)**0.5)/(2*a)

print('nilai x1 = {:.2f}'.format(x1))
print(f'nilai x2 = {x2:.2f}')