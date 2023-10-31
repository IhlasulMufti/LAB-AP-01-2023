import os
import random
import datetime

pembatas = '='*87

def history(riwayat):
    if os.path.exists('History.txt'):
        with open('History.txt', 'a') as file_history:
            for time, id_transaksi, total_harga in riwayat:
                file_history.write(f'|{time:<28}|{id_transaksi:<26}|Rp.{total_harga:>26}|\n')
                file_history.write(f'{pembatas}\n')
    else:        
        with open('History.txt', 'w') as file_history:
            file_history.write(f'{pembatas}\n')
            file_history.write(f'|{"RIWAYAT TRANSAKSI".center(len(pembatas))}')
            file_history.write(f'''
=======================================================================================
|            Waktu           |        ID Transaksi      |      Nominal Transaksi      |
=======================================================================================
''')
            for time, id_transaksi, total_harga in riwayat:
                file_history.write(f'''|{time:<28}|{id_transaksi:<26}|Rp.{total_harga:>26}|\n''')
                file_history.write(f'{pembatas}\n')

def invoice(transaksi,nama_kasir):
    riwayat = []
    time= datetime.datetime.now()
    angka_random = random.randint(100 ,999)
    nama = (nama_kasir).upper()
    result = ""
    for kata in nama.split():         
        result += kata[0]
    id_transaksi = f"{result}{time.strftime('%y%m%d%H%M%S')}{angka_random}"
    if not os.path.exists("invoices"):
        os.mkdir("invoices")
        print("File baru telah dibuat")
    filename = f"invoices/{id_transaksi}.txt"
    with open(filename, "w") as file:
        file.write(f"TOKO CAHAYA MORUT".center(len(pembatas)))
        file.write(f'\n{pembatas}\n')
        file.write(f"Nama kasir      : {nama_kasir}\n")
        file.write(f"Waktu Transaksi : {time.strftime('%d/%m/%y %H:%M')}\n")
        file.write(f'{pembatas}\n\n')
        file.write(f"Daftar Produk".center(len(pembatas)))
        print()
        file.write(f'''
    =============================================================================
    |      Nama Barang         |  Harga Satuan  | Jumlah Beli |       Total     |
    =============================================================================
''')
        total_harga = 0
        for nama_produk, harga_produk, jumlah1 in transaksi:
                if len(nama_produk) > 26:
                    nama_produk = nama_produk[:23] + '...'
                total = harga_produk * jumlah1
                total_harga += total  
                file.write(f'{"|":>5}{nama_produk:<26}|Rp. {harga_produk:>12}|{jumlah1:^13}|Rp.{total:>14}|\n')
        file.write(f'''    =============================================================================
''')
        file.write(f"{'|':>5}{'TOTAL':<57}| Rp. {total_harga:>12}|")  
        file.write(f'''
    =============================================================================
''')
        file.write(f'''
=======================================================================================
                             TERIMA KASIH TELAH BERBELANJA
=======================================================================================
''')
    riwayat.append((time.strftime('%d/%m/%y %H:%M'), id_transaksi, total_harga))
    
    history(riwayat)
    return filename

def program():
    kata = "SELAMAT DATANG"
    kata1 = "TRANSAKSI BERHASIL"
    print(pembatas)
    print(f"{kata.center(len(pembatas))}")
    print(pembatas)
    nama_kasir = input("Masukkan nama kasir : ").capitalize()
    while True:
        print(pembatas)
        print("Pilih opsi:")
        print('''
    1. Transaksi Baru
    2. Cari transaksi
    3. Keluar 
            ''')
        print(pembatas)
        pilih = int(input("Masukkan opsi pilihan : "))
        print(pembatas)
        transaksi = []
        match pilih:
            case 1:
                while True:
                    produk = input("Masukkan nama produk : ")
                    harga = int(input("Masukkan harga produk : "))
                    jumlah = int(input("Masukkan jumlah barang : "))
                    print(pembatas)
                    tambah = input("Tambah produk? (y/t) : ") 
                    transaksi.append((produk, harga, jumlah))
                    if tambah == 'y':
                        print(pembatas)
                        continue
                    elif tambah == 't':
                        print(pembatas)
                        print(f"{kata1.center(len(pembatas))}")
                        invoice(transaksi,nama_kasir)
                        break
                    else:
                        print("input tidak valid")
                        tambah = input("Tambah produk? (y/t) : ")
                        if tambah == 'y':
                            continue
                        elif tambah == 't':
                            print(pembatas)
                            print(f"{kata1.center(len(pembatas))}")
                            print(pembatas)
                            break
                        continue
                        
            case 2:
                cek = input("Masukkan ID transaksi : ")
                try:
                    with open(f"invoices/{cek}.txt", "r") as file_transaksi:
                        print(f'\n\n{file_transaksi.read()}')
                        break
                except FileNotFoundError:
                    print("File Transaksi tidak ditemukan")
                    break
            case 3:
                print(f'{"SAMPAI JUMPA".center(len(pembatas))}')
                print(pembatas)
                exit()
            case _:
                print("Opsi tidak tersedia")
                break
program()
                