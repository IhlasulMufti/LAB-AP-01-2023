import os
import datetime
import random

transaksi = []

def buat_file(kasir, sekarang):
    inisial = "".join(kata[0] for kata in kasir.split())
    tanggal_transaksi = sekarang.strftime('%y%m%d%H%M')
    angka_acak = random.randint(100, 999)
    id_transaksi = inisial + tanggal_transaksi + str(angka_acak)
    return id_transaksi

def cari_invoice(id_transaksi):
    if os.path.exists(f"invoices/{id_transaksi}.txt"):
        with open(f"invoices/{id_transaksi}.txt", "r") as file:
            isi_invoice = file.read()
        print(isi_invoice)
    else:
        print(f"Invoice dengan ID {id_transaksi} tidak ditemukan.")

def riwayat_transaksi(id_transaksi, waktu, total_semua):
    with open(f"invoices/trx_history.txt", "a") as file:
        file.write(f"\n| {waktu.center(19)} | {id_transaksi.center(21)} | {total_semua.rjust(20)} |")

def proses(opsi, kasir, transaksi):
    if opsi == '1':
        produk = input(f'Masukkan nama produk         : ')
        while True:
            try:
                harga = int(input(f'Masukkan harga produk        : '))
                break
            except:
                print(f"{'='*70}\nMohon masukkan angka\n{'='*70}")
        
        while True:
            try:
                jumlah = int(input(f'Masukkan jumlah produk       : '))
                break
            except:
                print(f"{'='*70}\nMohon masukkan angka\n{'='*70}")

        transaksi.append((produk, harga, jumlah))
        print("=" * 70)
        while True : 
            tanya = input(f'Tambah produk? (Ya/Tidak)    : ').lower()
            print("=" * 70)
            if tanya != 'ya' and tanya != 'tidak':
                print("Mohon masukkan antara Ya/Tidak")
            else :
                break
        if tanya == 'tidak':
            folder_path = "invoices"
            if not os.path.exists(f"{folder_path}"):
                os.mkdir(f"{folder_path}")
            sekarang = datetime.datetime.now()
            waktu_transaksi = sekarang.strftime('%d/%m/%y %H:%M')
            id_transaksi = buat_file(kasir, sekarang)
            judul = ("TOKO " + kasir)
            with open(f"invoices/{id_transaksi}.txt", "w") as file:
                file.write(f"{judul.center(70)}\n\n{'='*70}")
                file.write(f"\nNama kasir             : {kasir}")
                file.write(f"\nWaktu transaksi        : {sekarang.strftime('%d/%m/%y %H:%M')}\n{'='*70}")
                file.write(f"\n\n{'Daftar Produk'.center(70)}")
                file.write(f"\n\n{('='*60).center(70)}")
                file.write(f"\n     | {'Nama'.center(17)} | {'Harga'.center(10)} | Jumlah | {'Total'.center(14)} |\n{('='*60).center(70)}")
                total_simpan = [] 
                for produk, harga, jumlah in transaksi:
                    total = harga * jumlah
                    total_satuan = "Rp" + str(total)
                    harga = "Rp" + str(harga)
                    jumlah = str(jumlah)
                    if len(produk) > 17:
                        produk = produk[:14] + "..."
                    file.write(f"\n     | {produk.ljust(17)} | {harga.rjust(10)} | {jumlah.center(6)} | {total_satuan.rjust(14)} |")
                    total_simpan.append(total)  
                total_semua = "Rp" + str(int(sum(total_simpan)))
                file.write(f"\n{('='*60).center(70)}\n     | {'TOTAL'.center(20)} {'|'.rjust(20)} {total_semua.rjust(14)} |\n{('='*60).center(70)}\n")
            with open(f"invoices/{id_transaksi}.txt", "a") as file:
                file.write(f"\n\n{'='*70}\n{'TERIMA KASIH TELAH BERBELANJA'.center(70)}\n{'='*70}")
            if not os.path.exists(f"invoices/trx_history.txt"):
                with open(f"invoices/trx_history.txt","w") as file:
                    file.write(f"\n{'RIWAYAT TRANSAKSI'.center(70)}\n\n{'='*70}")
                    file.write(f"\n| {'WAKTU'.center(19)} | {'ID TRANSAKSI'.center(21)} | {'NOMINAL TRANSAKSI'.center(20)} |\n{'='*70}")
            riwayat_transaksi(id_transaksi, waktu_transaksi, total_semua)
            closing = "TRANSAKSI DENGAN ID : " + id_transaksi + " BERHASIL DIBUAT"
            print(f"\n{'='*70}\n{closing.center(70)}\n{'='*70}")
            transaksi.clear()
        elif tanya == 'ya':
            proses(opsi, kasir, transaksi)
    elif opsi == '2':
        id_transaksi = input("Masukkan ID transaksi        : ")
        print("=" * 70)
        cari_invoice(id_transaksi)
    elif opsi == '3':
        print(f"{'TERIMA KASIH TELAH BERKERJA'.center(70)}\n{'='*70}")
        exit()
    else:
        print("Mohon pilih antara 1, 2, atau 3")

''' PROGRAM UTAMA DIMULAI DISINI '''

while True:
    print(f'{"=" *70}\n{"SELAMAT DATANG".center(70)}\n{"=" *70}')
    kasir = input(f"Masukkan nama kasir{': '.rjust(12)}").upper()
    print('=' * 70)

    while True:
        print(f"Pilih opsi : \n1. Transaksi baru\n2. Cari Transaksi\n3. Keluar\n{'='*70}")
        opsi = input(f"Masukkan opsi pilihan        : ")
        print("=" * 70)
        proses(opsi, kasir, transaksi)