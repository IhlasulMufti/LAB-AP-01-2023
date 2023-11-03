def maksimum(x):
    maks = x[0]
    for i in x: 
        if i >= maks:
            maks = i
    return print(maks)
x = []
while True:
    try:
        n = input('Masukkan input: ').lower()
        if  n == 'selesai':
            break
        n = int(n)
        x.append(n)
    except ValueError:            
        print('Inputan harus berupa integer.')
        exit()

maksimum(x)