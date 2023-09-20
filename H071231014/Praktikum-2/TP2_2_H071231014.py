a = input('Masukan Input Pertama :')
b = input('Masukan Input Kedua :')
c = input('Masukan Input Ketiga :')

if a == 'vertebrado':
    if b == 'ave':
        if c =='carnivoro':
            print('aguia')
        elif c == 'onivoro': 
            print('pomba')
        else:
            print('invalid input')
    if b == 'mamifero':
        if c =='onivoro':
            print('homem')
        elif c =='herbivoro':
            print('vaca')
        else:
            print('invalid input')

elif a == 'intervebrado':
    if b == 'inseto':
        if c == 'hemtofago':
            print('pulga')
        elif c == 'herbivoro':
            print('lagarta')
        else:
            print('invalid input')
    if b == 'anelideo':
        if c == 'hematofago':
            print('sanguessuga')
        elif c == 'anovoro':
            print('minhoca')
        else:
            print('invalid input')
else:
    print('invalid input')