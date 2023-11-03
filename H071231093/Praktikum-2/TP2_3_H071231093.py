#Meminta input
Golongan = str(input("Golongan = ")).upper()
Daya = int(input("Daya = "))
Pemakaian = int(input("Pemakaian = "))
hasil = 0

#Variabel Rumus
if Golongan == "R1" :
    if 0 < Daya <= 900 :
        hasil = Pemakaian * 1352
    elif 901 < Daya <= 1300 :
        hasil = Pemakaian * 1444.70
    elif 1301 < Daya <= 2200 :
        hasil = Pemakaian * 1444.70
    else:
        print("Data Tidak Valid")
elif Golongan == "R2" :
    if 3500 <= Daya <= 5500 :
        hasil = Pemakaian * 1699.53
    else:
        print("Data Tidak Valid")
elif Golongan == "R3" :
    if Daya >= 6600:
        hasil = Pemakaian * 1699.53
    else:
        print("Data Tidak Valid")
elif Golongan == "B2" :
    if 6600 <= Daya <= 200000 :
        hasil = Pemakaian * 1444.70
    else:
        print("Data Tidak Valid")
elif Golongan == "B3" :
    if Daya > 200000 :
        hasil = Pemakaian * 1114.74
    else:
        print("Data Tidak Valid")
elif Golongan == "I3" :
    if Daya >= 200000 :
        hasil = Pemakaian * 1314.12
    else:
        print("Data Tidak Valid")
elif Golongan == "P1" :
    if 6600 <= Daya <= 200000 :
        hasil = Pemakaian * 1523.28
    else:
        print("Data Tidak Valid")
else:
    print("Data Tidak Valid")

print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp, {hasil:,.1f}".replace(',','@').replace('.',',').replace('@','.'))