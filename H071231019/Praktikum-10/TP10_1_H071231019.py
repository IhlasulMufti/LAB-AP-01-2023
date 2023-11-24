import re
import os

class DataPengguna:
    def __init__(self):
        self.data = {'Nama': '', 'Email': '', 'Password': ''}

    def kosong(self):
        return all(value == '' for value in self.data.values())

    def detail_anda(self):
        if self.kosong():
            print('Data saat ini kosong')
        else:
            for key, value in self.data.items():
                print(f'{key}: {value}')

    def ubah_nama(self):
        if self.kosong():
            print('Data saat ini kosong')
        else:
            namabaru = input('Masukkan nama baru: ')
            self.data['Nama'] = namabaru
            print('Nama berhasil diubah')

    def simpan_data(self):
        if self.kosong():
            print('Data saat ini kosong')
        else:
            namafile = input('Masukkan nama file tanpa (.txt): ') + '.txt'
            if os.path.exists(namafile):
                with open(namafile, 'a') as file:
                    for key, value in self.data.items():
                        file.write(f'|{key}: {value}\n')
                    file.write(f"+{'='*99}\n")

            else:
                with open(namafile, 'w') as file:
                    file.write(f"+{'='*99}\n")
                    file.write(f"|Data yang tersimpan\n")
                    file.write(f"+{'='*99}\n")
                
                    for key, value in self.data.items():
                        file.write(f'|{key}: {value}\n')
                    file.write(f"+{'='*99}\n")
            
            self.data = {}
            print('Data berhasil disimpan')

    def data_baru(self):
        name = input("Masukkan Nama: ")
        while True:
        # Input Email
            email = input("Masukkan Email: ")
            if re.match(r"[a-z0-9._%+-]+@student\.unhas\.ac\.id$", email):
                break
            else:
                print("Email yang Anda Masukkan Salah. Silakan coba lagi.")
        
        while True:
        # Input Password
            password = input("Masukkan Password: ")
            if 8 <= len(password) <= 20 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
                break
            else:
                print("Password tidak memenuhi syarat. Silakan coba lagi.")

        self.data["Nama"] = name
        self.data["Email"] = email
        self.data["Password"] = password
        print("Data berhasil dibuat")
  # Exit the loop if everything is valid

def main():
    user_data = DataPengguna()

    while True:
        print(f"{'='*50}")
        print("Menu:")
        print("1. Detail Anda")
        print("2. Ubah Nama")
        print("3. Jumlah Data pada File")
        print("4. Save Data pada File")
        print("5. Buat Data Baru")
        print("6. Keluar")
        print(f"{'='*50}")
        pilihan = input('Pilih menu yang anda inginkan: ').lower()
        print(f"{'='*50}")
        if pilihan == '1':
            user_data.detail_anda()
            print(f"{'='*50}")
        elif pilihan == '2':
            user_data.ubah_nama()
            print(f"{'='*50}")
        elif pilihan == '3':
            file_name = input("Masukkan nama file tanpa format (.txt): ") + '.txt'
            if not os.path.exists(file_name):
                print(f"{'='*50}")
                print(f"Tidak Terdapat File Dengan Nama {file_name[:-4]}")
                print("Jumlah data pada file berjumlah 0")
            else:
                with open(file_name, mode="r") as cari_data:
                    pattern_jumlah = re.findall(r"\|Nama: ", cari_data.read())
                    print(f"{'='*50}")
                    print("File Ditemukan")
                    print(f"Jumlah data pada file berjumlah {len(pattern_jumlah)}")
            print(f"{'='*50}")
        elif pilihan == '4':
            user_data.simpan_data()
            print(f"{'='*50}")
        elif pilihan == '5':
            user_data.data_baru()
            print(f"{'='*50}")
            pass
        elif pilihan == '6':
            print('Sampai Jumpa Lagi')
            print(f"{'='*50}")
            break
        else:
            print('Pilihan tidak valid. Masukkan pilihan yang benar (1-6).')
            print(f"{'='*50}")

main()