import re
import os
class UserData:
    def __init__(self,nama="",email="",password=""):
        self.nama = nama
        self.email = email
        self.password = password

    def validate_email(self):
        pola = r"^[a-z]+(?:\d{0,})?@student\.unhas\.ac\.id$"
        return re.match(pola,self.email)
    
    def validate_password(self):
        pola = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,20}$"
        return re.match(pola,self.password)
    
    def tampilkan_data(self):
        if not self.nama and not self.email and not self.password:
            print("="*50)
            print("Data saat ini kosong")
        else:
            print("="*50)
            print(f"Data Anda:")
            print(f"Nama:{self.nama}")
            print(f"Email:{self.email}")
            print(f"Password:{self.password}")

    def mengubah_nama(self):
        if not self.nama:
            print("="*50)
            print("Data saat ini kosong")
        else:
            print("="*50)
            self.nama = input("Silahkan Input Nama Baru: ")
            print("="*50)

    def membuat_data_baru(self): 
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

    def simpan_data_kefile(self):
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
+{"="*60}
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

        opsi = int(input("Silahkan Pilih Opsi Anda: "))

        match opsi:
            case 1:
                user_data.tampilkan_data()
            case 2:
                user_data.mengubah_nama()
            case 3:
                filenama = input("Masukkan Nama File (tanpa format .txt): ")

                if not filenama.endswith(".txt"):
                    filenama += ".txt"

                if os.path.exists(filenama):
                    with open(filenama, "r") as file:
                        line = len(file.readlines())
                        panjang = (line - 3)//4
                        print(f"Jumlah Data pada File {filenama}: {panjang}")
                else:
                    print("="*50)
                    print(f"Tidak Terdapat File dengan Nama {filenama}")
            case 4:
                user_data.simpan_data_kefile()
            case 5:
                user_data.membuat_data_baru()
            case 6:
                print("="*50)
                print("Sampai Jumpa Lagi")
                print("="*50)
                break
            case _:
                print("Pilihan tidak tersedia. Silakan pilih opsi yang valid.")

