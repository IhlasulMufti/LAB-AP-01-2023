import os
import random
import datetime

def kolom(Kata,panjang):
    kata = str(Kata)
    if len(kata) >= panjang:
        Kata = kata[:(panjang-3)] + ("." * 3)
    else:
        Kata = kata + (" " * (panjang - len(kata)))
    return Kata

def inisial_kasir(nama):
    panjang_string = len(nama)
    if panjang_string < 3:
        return "Panjang nama harus lebih dari 2 karakter."
    if panjang_string%2==0:
        index_tengah = panjang_string // 2
        hasil = nama[0] + nama[index_tengah-1] + nama[index_tengah] + nama[-1]
    else:
        index_tengah = panjang_string // 2
        hasil = nama[0] + nama[index_tengah] + nama[-1]
    hasil = str(hasil).upper()
    return hasil

def buat_history(id_transaksi,harga_total,tahun,bulan,hari,jam,menit):

    waktu = tahun + '/' + bulan + '/' + hari + ' ' + jam + ':' + menit
    
    if os.path.exists(f"{os.path.dirname(__file__)}/trx_history.txt") == False and os.path.isdir(f"{os.path.dirname(__file__)}/trx_history.txt") == False:
        with open(f"{os.path.dirname(__file__)}/trx_history.txt",'w') as file:
            file.write(f"{' '*24}RIWAYAT TRANSAKSI\n")
            file.write(f"{'='*73}")
            file.write(f"\n|{kolom('Waktu',17)}|{kolom('ID Transaksi',25)}|{kolom('Nominal Transaksi',27)}|\n")
            file.write(f"{'='*73}\n")

    with open(f"{os.path.dirname(__file__)}/trx_history.txt",'a') as file:
        file.write(f"|{kolom(waktu,17)}|{kolom(id_transaksi,25)}|{kolom(harga_total,27)}|\n")
        file.write(f"{'='*73}\n")

def buat_invoice(transaksi,nama_kasir):
    harga_total = 0
    # ini untuk membuat folder jika tidak ada
    invoices_folder = os.path.join(os.path.dirname(__file__), "invoices")
    if os.path.exists(invoices_folder) == False and os.path.isdir(invoices_folder) == False:
        os.mkdir(invoices_folder)
        
    tahun = str(datetime.datetime.now().year)[-2:]  # Mengambil 2 digit terakhir tahun
    bulan = f"{datetime.datetime.now().month:02}"  # Format bulan 2 digit (dengan 0 di depan jika hanya 1 digit)
    hari = f"{datetime.datetime.now().day:02}"  # Format hari 2 digit (dengan 0 di depan jika hanya 1 digit)
    jam = f"{datetime.datetime.now().hour:02}"  # Format jam 2 digit (dengan 0 di depan jika hanya 1 digit)
    menit = f"{datetime.datetime.now().minute:02}"  # Format menit 2 digit (dengan 0 di depan jika hanya 1 digit)

    id_transaksi = inisial_kasir(nama_kasir) + tahun + bulan + hari + jam + menit + str(random.randint(100, 999))


    with open(f"{invoices_folder}/{id_transaksi}.txt","w") as file:
        # penggunaan spasi dibadingkan \t adalah untuk menghindari format yang tidak konsisten jika dibuka menggunakan notepad
        file.write(f"{' '*32}TOKO YUSRAN\n")
        file.write(f"{'='*80}\n")
        file.write(f"Nama Kasir \t: {nama_kasir}\n")
        file.write(f"{' '*32}DAFTAR PRODUK\n")
        file.write(f"{' '*4}{'='*73}")
        file.write(f"\n{' '*4}|{kolom('Nama Barang',17)}|{kolom('Harga Barang',17)}|{kolom('Jumlah',17)}|{kolom('Total',17)}|\n")

        for i in range(len(transaksi["nama"])):
                formatted_harga = f"Rp {transaksi['harga'][i]:,.0f}"  # Format harga dalam nominal
                formatted_total = f"Rp {transaksi['total'][i]:,.0f}"  # Format total dalam nominal

                file.write(f"{' '*4}|{kolom(transaksi['nama'][i],17)}|{kolom(formatted_harga,17)}|{kolom(transaksi['jumlah'][i],17)}|{kolom(formatted_total,17)}|\n")
                harga_total += transaksi['total'][i]
        
        formatted_harga_total = f"Rp {harga_total:,.0f}"  # Format total harga keseluruhan
        file.write(f"{' '*4}{'='*73}")
        file.write(f"\n{' '*4}|{kolom(' ',17)} {kolom('Total',17)} {kolom(' ',17)}|{kolom(formatted_harga_total,17)}|")
        file.write(f"\n{' '*4}{'='*73}")
        file.write(f"\n{'='*80}\n")
        file.write(f"{' '*28}TERIMA KASIH TELAH BERBELANJA")
        file.write(f"\n{'='*80}\n")

    buat_history(id_transaksi,formatted_harga_total,tahun,bulan,hari,jam,menit)
    print("=" * 50)
    print(" " * 20 + "TRANSAKSI BERHASIL")


def cari_transaksi():
    invoices_folder = os.path.join(os.path.dirname(__file__), "invoices")
    if os.path.exists(invoices_folder) == False and os.path.isdir(invoices_folder) == False:
        print("Belum Ada Transaksi")
    else:
        print("DAFTAR TRANSAKSI")
        for nama_file in os.listdir(invoices_folder):
            print(nama_file[:-4])

        nama_transaksi = input("Masukkan Nama Transaksi : ")
        print("=" * 50)
        with open(f"{invoices_folder}/{nama_transaksi}.txt","r") as file:
            for line in file.readlines():
                print(line)


def transaksi_baru(nama_kasir):
    transaksi = {
        "nama": [],
        "harga": [],
        "jumlah": [],
        "total":[],
    }
    
    tambah_lagi = True

    while tambah_lagi:
        transaksi["nama"].append(input("Masukkan Nama Produk : "))
        harga = int(input("Masukkan Harga Produk : "))
        transaksi["harga"].append(harga)
        jumlah = int(input("Masukkan Jumlah Produk : "))
        transaksi["jumlah"].append(jumlah)
        transaksi["total"].append(harga * jumlah)
        print("=" * 50)

        while True:
            user_input = input("Tambah Produk? (y/t): ").lower()
            if user_input == "y":
                tambah_lagi = True
                break
            elif user_input == "t":
                tambah_lagi = False
                break
            else:
                print("Masukan tidak valid. Mohon masukkan 'y' untuk Ya, 't' untuk Tidak.")
        
    buat_invoice(transaksi,nama_kasir)
    
def input_data(nama_kasir):
    print("=" * 50)
    print("Pilih Opsi :\n1. Transaksi Baru\n2. Cari Transaksi\n3. Keluar")
    print("=" * 50)
    opsi = int(input("Masukkan Opsi Pilihan : "))
    print("=" * 50)
    match opsi:
        case 1:
            transaksi_baru(nama_kasir)
            input_data(nama_kasir)
        case 2:
            cari_transaksi()
            input_data(nama_kasir)
        case 3:
            print(" " * 20 + "TERIMA KASIH")
            print("=" * 50)
            quit()
        case _:
            print("Masukkan Pilihan Yang Benar!!")
            input_data(nama_kasir)
        

print("=" * 50)
print(" " * 20 + "SELAMAT DATANG")
print("=" * 50)
nama_kasir = input("Masukkan Nama Kasir \t: ")
input_data(nama_kasir)
