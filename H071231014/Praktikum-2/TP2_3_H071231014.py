#informasi daya listrik dan total tagihan 
golongan = input('Golongan =')
daya = int(input('Daya ='))
pemakaian = int(input('Pemakaian ='))

match golongan:
    case 'R1':
        if daya == 900:
            tagihan= pemakaian*1352
        elif daya == 1300:
            tagihan= pemakaian*1444.70     
        elif daya == 2200 :
            tagihan= pemakaian*1444.70
    case 'R2':
        if 3500 <= daya <= 5500:
            tagihan= pemakaian*1699.53
    case 'R3':
        if daya >= 6600:
            tagihan= pemakaian*1699.53
        if 6600 <= daya <= 200000:
            tagihan= pemakaian*1444.70
    case 'B3':
        if daya >= 200000:
            tagihan= pemakaian*1114.74
    case 'I3':
        if daya >= 200000:
            tagihan= pemakaian*1314.12
    case 'P1':
        if 6600 <= daya <=200000:
            tagihan= pemakaian*1523.28
    case _:
        print('data tidak valid')
print(f'jumlah tagihan anda sebesar : Rp {tagihan:,.1f}'.replace(',','x').replace('.',',').replace('x','.'))