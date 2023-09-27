
# print(f"\n{'='*33}\nPenghitung Jumlah Tagihan Listrik\n{'='*33}\n")
print("Penghitung Jumlah Tagihan Listrik")

# Input golongan 
print("Golongan : R1, R2, R3, B2, B3, I3, P1 ")
gol = input("Golongan = ")

if gol not in['R1','R2','R3','B2','B3','I3','P1']:
    print("\nInvalid data.\n")
    quit()

# Input daya
daya = input("\nDaya: ")
if daya.isdigit() == False:
    print("\nInvalid data.\n")
    quit()
daya = int(daya)

# Penentuan tarif per kWh
match gol:
    case 'R1':
        if daya == 900:
            TARIF = 1352
        elif daya == 1300 or daya == 2200:
            TARIF = float(1444.70)
        else:
            print("\nInvalid data.\n")
            quit()
                
    case 'R2':  
        if 3500 <= daya <= 5500:
            TARIF = 1699.53
        else:
            print("\nInvalid data.\n")
            quit()

    case 'R3':     
        if daya >= 6600:
            TARIF = 1699.53
        else:
            print("\nInvalid data.\n")
            quit()

    case 'B2': 
        if 6600 <= daya <= 200000:
            TARIF = 1444.70
        else:
            print("\nInvalid data.\n")
            quit()

    case 'B3':        
        if daya > 200000:
            TARIF = 1114.74
        else:
            print("\nInvalid data.\n")
            quit()

    case 'I3':      
        if daya >= 200000:
            TARIF = 1314.12
        else:
            print("\nInvalid data.\n")
            quit()

    case 'P1':        
        if 6600 <= daya <= 200000:
            TARIF = 1523.28
        else:
            print("\nInvalid data.\n")
            quit()

    case _:
        print("Invalid input.")
        quit()

# Input pemakaian
pakai = input("Pemakaian: ")
if pakai.isdigit() == False:
    print("\nInvalid data.\n")
    quit()
pakai = int(pakai)

# Menghitung jumlah tagihan sesuai dengan data yang telah dimasukkan
tagihan = float(TARIF * pakai)

# Mengatur format tulisan jumlah tagihan sesuai dengan Kaidah Bahasa Indonesia dan mencetak jumlah tagihan
depan,koma = str(tagihan).split('.')
depan = int(depan); koma = koma[:2]
depan = f"{depan:,}".replace(',',".")
print('\nJumlah tagihan Anda sebesar: Rp.{},{}\n'.format(depan,koma))

# print('\nJumlah tagihan Anda sebesar: Rp{}\n'.format(tagihan))

