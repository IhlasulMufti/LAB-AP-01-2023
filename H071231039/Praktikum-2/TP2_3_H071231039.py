gol = input('Golongan= ')
day = float(input('Daya= '))
pem = float(input('Pemakaian= '))

match gol:
    case 'R1':
        if day == 900:
            tagihan = pem*1352
        elif day == 1300:
            tagihan = pem*1444.70
        elif day == 2200:
            tagihan = pem*1444.70
        else:
            print('data tidak valid')
    case 'R2':
        if day >= 3500 and day <= 5500:
            tagihan = pem*1699.53
        else:
            print('data tidak valid')
    case 'R3':
        if day >= 6600:
            tagihan = pem*1699.53
        else:
            print('data tidak valid')
    case 'B2':
        if day >= 6600 and day <= 200000:
            tagihan = pem*1444.70
        else:
            print('data tidak valid')
    case 'B3':
        if day > 200000:
            tagihan = pem*1114.74
        else:
            print('data tidak valid')
    case 'I3':
        if day >= 200000:
            tagihan = pem*1314.12
        else:
            print('data tidak valid')
    case 'P1':
        if day >= 6600 and day <= 200000:
            tagihan = pem*1523.28
        else:
            print('data tidak valid')
    case _:
        print('data tidak valid')

print(f'Jumlah tagihan anda sebesar: Rp, {tagihan:,.1f}'.replace(
    ',', 'x').replace('.', ',').replace('x', '.'))