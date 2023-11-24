import re
import os

class UserData:
    def __init__(self, nama='', email='', password=''):
        self.nama = nama
        self.email = email
        self.password = password

    def validate_email(self):
        pattern = r"^[a-z]+(?:\d{1,})?@student.unhas.ac.id$"
        return re.match(pattern, self.email)

    def validate_password(self):
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,20}$"

        return re.match(pattern, self.password)

    def display_data(self):
        if not self.nama and not self.email and not self.password:
            print("="*50)
            print("Data saat ini kosong")
        else:
            print("="*50)
            print(f"Data Anda:\nNama     : {self.nama}\nEmail    : {self.email}\nPassword : {self.password}")
            
    def change_name(self):
        if not self.nama:
            print("="*50)
            print("Data saat ini kosong")
        else:
            print("="*50)
            self.nama = input("Silahkan Input Nama Baru: ")
            print("="*50)

    def create_new_data(self):
        print("="*50)
        self.nama = input("Masukkan Nama Anda     : ")

        while True:
            self.email = input("Masukkan Email Anda    : ")
            if not self.validate_email():
                print("Email yang Anda Masukkan Salah")
            else:
                break

        while True:
            self.password = input("Masukkan Password Anda : ")
            if len(self.password) < 8 or len(self.password) > 20:
                print("Password harus memiliki Panjang 8-20 karakter")
            elif not self.validate_password():
                print("Password yang Anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
            else:
                break

    def save_data_to_file(self): 
        if not self.nama and not self.email and not self.password:
            print("="*50)
            print("Data saat ini kosong")
        else:
            filename = input("Masukkan Nama File (tanpa format .txt): ")

            if not filename.endswith(".txt"):
                filename += ".txt"

            if os.path.exists(filename):
                with open(filename, "a") as file:
                    file.write(f'''|Nama     : {self.nama}
|Email    : {self.email}
|Password : {self.password}
+{"="*60} # untuk menampilkan garis horizontal panjang dengan 60 karakter "=".
''')
            else:
                with open(filename, "w") as file:
                    file.write(f'''+{"="*60}
| Data yang Tersimpan
+{"="*60}                              
|Nama     : {self.nama}
|Email    : {self.email}
|Password : {self.password}
+{"="*60}
''')
                print("File berhasil dibuat")
            print("Berhasil menyimpan data ke file")
            # Reset data
            self.nama = ""
            self.email = ""
            self.password = ""

user_data = UserData()
while True:
        print("="*50)
        print("Selamat Datang! Silahkan Pilih Opsi Menu Anda:")
        print("1. Detail Anda")
        print("2. Ubah Nama")
        print("3. Jumlah Data pada File")
        print("4. Save Data pada File")
        print("5. Buat Data Baru")
        print("6. Keluar")

        pilihan = input("Silahkan Pilih Opsi Anda: ")

        if pilihan == "1":
            user_data.display_data()

        elif pilihan == "2":
            user_data.change_name()

        elif pilihan == "3":
            filename = input("Masukkan Nama File (tanpa format .txt): ")

            if not filename.endswith(".txt"):
                filename += ".txt"

            if os.path.exists(filename):
                with open(filename, "r") as file:
                    lines = len(file.readlines())
                    panjang = (lines - 3)//4
                    print(f"Jumlah Data pada File {filename}: {panjang}")
            else:
                print("="*50)
                print(f"Tidak Terdapat File dengan Nama {filename}")

        elif pilihan == "4":
            user_data.save_data_to_file()

        elif pilihan == "5":
            user_data.create_new_data()

        elif pilihan == "6":
            print("="*50)
            print("Sampai Jumpa Lagi")
            print("="*50)
            break
        else:
            print("Pilihan tidak tersedia. Silakan pilih opsi yang valid.")