golongan = input("Golongan = ").upper()
daya = int(input("Daya = "))
pemakaian = float(input("Pemakaian = "))

match (golongan, daya):
    case ("R1", 900):
        tagihan = 1352 * pemakaian
    case ("R1", 1300) | ("R1", 2200):
        tagihan = 1444.7 * pemakaian
    case ("R2", _) if 3500 <= daya <= 5500:
        tagihan = 1699.53 * daya
    case ("R3", _) if daya >= 6600:
        tagihan = 1699.53 * daya
    case ("B2", _) if 6600 <= daya <= 200000:
        tagihan = 1444.7 * daya
    case ("B3", _) if daya >= 200000:
        tagihan = 1114.74 * daya
    case ("I3", _) if daya >= 200000:
        tagihan = 1314.12 * daya
    case ("P1", _) if 6600 <= daya <= 200000:
        tagihan = 1523.28 * daya
    case _:
        print("data tidak valid")

print(f"Jumlah tagihan Anda sebesar: Rp{tagihan:.1f}".replace('.', 'suci').replace(',', '.').replace('suci', ','))