Harga = int(input("Masukkan Harga barang: "))
Pembayaran = int(input("Masukkan Uang Anda: "))
Kembalian = Pembayaran - Harga

seratus = 0
limapuluh = 0
duapuluh  = 0
sepuluh   = 0
limaribu  = 0
duaribu  = 0
seribu  = 0

while Kembalian > 0: #while: untuk mengulang proses kembalian uang hingga kembalian mencapai
# nol atau kurang. # kembalian > 0: loop ini akan terus berjalan selama kembalian lebih dari nol.
# >=: untuk memeriksa apakah kembalian lebih besar atau sama dengan 0
# +=: menambahkan nilai pada variabel dengan nilai lain, nilai pada variabel seratus akan ditambah 1
# -=: mengurangkan nilai pada variabel dengan nilai lain, nilai pada variabel seratus akan ditambah 1
    if Kembalian >= 100000:
        seratus += 1
        Kembalian -= 100000
    elif Kembalian >= 50000:
        limapuluh += 1
        Kembalian -= 50000
    elif Kembalian >= 20000: 
        duapuluh += 1
        Kembalian -= 20000
    elif Kembalian >= 10000:
        sepuluh += 1
        Kembalian -= 10000
    elif Kembalian >= 5000:
        limaribu += 1
        Kembalian -= 5000
    elif Kembalian >= 2000:
        duaribu += 1
        Kembalian -= 2000
    elif Kembalian >= 1000:
        seribu += 1
        Kembalian -= 1000

print(f"uang kembalian kurang dari harga barang yang di beli")

"break"
print(f"{seratus} uang sejumlah RP 100.000")
print(f"{limapuluh} uang Sejumlah RP 50.000")
print(f"{duapuluh} uang Sejumlah RP 20.000")
print(f"{sepuluh} uang Sejumlah RP 10.000")
print(f"{limaribu} uang Sejumlah RP 5.000")
print(f"{duaribu} uang Sejumlah RP 2.000")
print(f"{seribu} uang Sejumlah RP 1.000")