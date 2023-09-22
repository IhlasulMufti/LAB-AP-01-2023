golongan = input('Golongan = ').upper()
daya = float(input('Daya = '))
pemakaian = float(input('Pemakaian = '))

tarif_per_kwh = 0

if golongan == 'R1':
    if daya == 900:
        tarif_per_kwh = 1352
    elif daya == 1300:
        tarif_per_kwh = 1444.70
    elif daya == 2200:
        tarif_per_kwh = 1444.70
elif golongan == 'R2':
    if 3500 <= daya <= 5500:
        tarif_per_kwh = 1699.53
elif golongan == 'R3':
    if daya >= 6600:
        tarif_per_kwh = 1699.53
elif golongan == 'B2':
    if 6600 <= daya <= 200000:
        tarif_per_kwh = 1444.70
elif golongan == 'B3':
    if daya > 200000:
        tarif_per_kwh = 1114.74
elif golongan == 'I3':
    if daya >= 200000:
        tarif_per_kwh = 1314.12
elif golongan == 'P1':
    if 6600 <= daya <= 200000:
        tarif_per_kwh = 1523.28

tagihan = pemakaian * tarif_per_kwh

if tarif_per_kwh > 0:
    print(f'Pemakaian = Jumlah tagihan anda sebesar : Rp {tagihan:,.1f}'.replace('.','#').replace(',','.').replace('#',','))
else:
    print('Data tidak valid.')