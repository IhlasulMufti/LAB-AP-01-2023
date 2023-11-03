gol = (input("Golongan: "))
daya = int(input("Daya (VA): "))
pemakaian = int(input("Pemakaian (kWh): "))
tarif_per_kWh = 0

if gol == "R1":
    if daya == 900:
        tarif_per_kWh = 1352
    elif daya == 1300:
        tarif_per_kWh = 1444.70
    elif daya == 2200:
        tarif_per_kWh = 1444.70
elif gol == "R2" and 3500 >= daya <= 5500:
    tarif_per_kWh = 1699.53
elif gol == "R3" and daya > 6600:
    tarif_per_kWh = 1699.53
elif gol == "B2" and 6600 >= daya <= 200000:
    tarif_per_kWh = 1444.70
elif gol == "B3" and daya > 200000:
    tarif_per_kWh = 1114.74  
elif gol == "I3" and daya > 200000:
    tarif_per_kWh = 1314.12  
elif gol == "P1" and 6600 >= daya <= 200000:
    tarif_per_kWh = 1523.28  

harga = (tarif_per_kWh * pemakaian)
if harga > 0:
    print(f"pemakaian = Jumlah tagihan anda: Rp {harga:,.1f} ")