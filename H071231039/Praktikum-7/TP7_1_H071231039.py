import os
import datetime
import random

def AAA() :
    print("=" * 70)

def dataHistory() :
    with open("history", "w") as file :
        file.write(f"{'='*70}\n")
        file.write(f"|{'RIWAYAT TRANSAKSI':^68}|\n")
        file.write(f"{'='*70}\n")
        file.write(f"|{'Waktu':^18}|{'ID Transaksi':^24}|{'Nominal Transaksi':^24}|\n")
        file.write(f"{'='*70}\n")
        file.close()

def addHistory(waktu,id,hasil) :
    with open("history", "a") as file:
        file.write(f"|{waktu:^18}|{id:^24}|{'Rp ' + str(hasil):^24}|\n")
        file.write(f"{'-'*70}\n")

def strukAtas(nama,waktu) :
    data.write(f"{'TOKO ALFAMARET':^70}\n\n")
    data.write(f"{'='*70}\n")
    data.write(f"Nama kasir\t:{nama}\n")
    data.write(f"Waktu transaksi:{waktu}\n")
    data.write(f"{'='*70}\n\n")
    data.write(f"{'Daftar Produk':^70}\n\n")
    data.write(f"{60*'=':^70}\n")
    data.write(f"{5*' '}|{'Nama':^23}|{'Harga':^12}|{'Jumlah':^8}|{'Total':^12}|\n")
    data.write(f"{60*'=':^70}\n")


def addStruk(produk, harga, jumlah, hasil) :
    data.write(f"{5*' '}|{produk:^23}|{harga:^12}|{jumlah:^8}|{hasil:>12}|\n")

def strukBawah(total_belanja):
    data.write(f"{60*'=':^70}\n")
    data.write(f"{' '*5}|{'TOTAL':^23}{' '*22}|{'Rp ' + str(total_belanja):>12}|\n")
    data.write(f"{60*'=':^70}\n\n")
    data.write(f"{'='*70}\n")
    data.write(f"{'TERIMA KASIH TELAH BERBELANJA':^70}\n")
    data.write(f"{'='*70}\n")

def ID_transaksi(nama) :
    inisial = nama[0] + nama[len(nama) // 2] + nama[-1]
    sekarang = datetime.datetime.now()
    tahun = str(sekarang.year % 2000)
    bulan = str(sekarang.month)
    tanggal = str(sekarang.day)
    jam = str(sekarang.hour) + str(sekarang.minute)
    angka = str(random.randint(100, 999))

    mr = str(inisial + tahun + bulan + tanggal + jam + angka )
    return mr

def waktu() :
    waktu = str(datetime.datetime.now()).replace("-","/")
    jam = waktu[2:16]
    return jam

folder_transaksi = "invoices"
if not os.path.exists("history") :
    dataHistory()

while True :
    AAA()
    print("SELAMAT DATANG".center(70))
    AAA()
    print("PILIH OPSI\t:\n1. Transaksi Baru\n2. Cari Transaksi\n3. Keluar")
    AAA()
    pilihan = input("Masukkan Opsi\t: ")
    AAA()
    match pilihan :
        case "1" :
            nama = input("Masukkan Nama Kasir\t: ").upper()
            AAA()
            id = ID_transaksi(nama)
            file_transaksi = os.path.join(folder_transaksi, id + ".txt")

            if not os.path.exists(folder_transaksi) :
                os.mkdir(folder_transaksi)

            data = open(file_transaksi, "a")
            time = waktu()

            strukAtas(nama,time)

            total_belanja = 0

            while True :
                produk = input("Masukkan Nama Produk\t: ")
                harga1 = int(input("Masukkan Harga Produk\t: "))
                jumlah = int(input("Masukkan Jumlah Produk\t: "))
                hasil1 = harga1*jumlah
                if len(str(hasil1)) >  6 :
                    hasil = str(hasil1 / 1000000) + "jt"
                else :     
                    hasil = (f"{hasil1:,}".replace(',','x').replace('.',',').replace('x','.'))
                
                total_belanja += (harga1 * jumlah)
                if len(str(total_belanja)) > 6 :
                    nominal = str(total_belanja / 1000000) + "jt"
                else :
                    nominal = (f"{total_belanja:,}".replace(',','x').replace('.',',').replace('x','.'))

                harga = (f"{harga1:,}".replace(',','x').replace('.',',').replace('x','.'))
                addStruk(produk,harga,jumlah,hasil)
                keluar_loop_luar = False
                while True:
                    lanjut = input("Tambah Produk? (y/t)\t: ")
                    if lanjut == "t":
                        strukBawah(nominal)
                        data.close()
                        keluar_loop_luar = True
                        break
                    elif lanjut == "y":
                        break
                    else:
                        print("Masukkan input y/t saja!")
                if keluar_loop_luar:
                    break
            addHistory(time,id,nominal)
        case "2":
            cari = input("Masukkan ID file yang ingin dicari : ")
            cari_path = folder_transaksi + "/" + cari + ".txt"
            if os.path.exists(cari_path):
                with open(cari_path, "r") as file:
                    print(file.read())
            else:
                print(f"File dengan ID {cari} tidak ditemukan")

        case "3":
            AAA()
            print("PROGRAM SELESAI".center(70))
            AAA()
            break
    
        case _:
            AAA()
            print("INPUT TIDAK VALID".center(70))
            AAA()