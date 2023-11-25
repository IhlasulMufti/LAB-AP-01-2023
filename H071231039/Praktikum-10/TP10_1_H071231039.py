import re
import os

class DataPengguna:
    def __init__(self):
        self.data = {'Nama': '', 'Email': '', 'Password': ''}

    def kosong(self):
        return all(value == '' for value in self.data.values())

    def detailanda(self):
        if self.kosong():
            print('Data saat ini kosong')
        else:
            for key, value in self.data.items():
                print(f'{key}: {value}')

    def ubahnama(self):
        if self.kosong():
            print('Data saat ini kosong')
        else:
            namabaru = input('Masukkan nama baru: ')
            self.data['Nama'] = namabaru
            print('Nama berhasil diubah')

    def simpandata(self):
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

            
    def databaru(self):
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
        print("a. Detail Anda")
        print("b. Ubah Nama")
        print("c. Jumlah Data pada File")
        print("d. Save Data pada File")
        print("e. Buat Data Baru")
        print("f. Keluar")
        print(f"{'='*50}")
        pilihan = input('Pilih menu yang anda inginkan: ').lower()
        print(f"{'='*50}")
        if pilihan == 'a':
            user_data.detailanda()
            print(f"{'='*50}")
        elif pilihan == 'b':
            user_data.ubahnama()
            print(f"{'='*50}")
        elif pilihan == 'c':
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
        elif pilihan == 'd':
            user_data.simpandata()
            print(f"{'='*50}")
        elif pilihan == 'e':
            user_data.databaru()
            print(f"{'='*50}")
            pass
        elif pilihan == 'f':
            print('Sampai Jumpa Lagi')
            print(f"{'='*50}")
            break
        else:
            print('Pilihan tidak valid. Masukkan pilihan yang benar (a-f).')
            print(f"{'='*50}")

if __name__ == "__main__":
    main()
