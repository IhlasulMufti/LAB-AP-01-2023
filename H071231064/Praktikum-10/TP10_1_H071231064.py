import re

class DataPengguna:
    def __init__(self):
        self.data = {
            'Nama': '',
            'Email': '',
            'Password': ''
        }

    def tampilkan_detail(self):
        if not self.data['Nama']:
            print("Data saat ini kosong")
        else:
            print("Detail Data:")
            for key, value in self.data.items():
                print(f"{key}: {value}")

    def ubah_nama(self):
        if not self.data['Nama']:
            print("Data saat ini kosong")
        else:
            new_name = input("Masukkan nama baru: ")
            self.data['Nama'] = new_name
            print("Nama berhasil diubah")

    def validasi_email(self, email):
        return re.match(r"[a-z0-9._%+-]+@student\.unhas\.ac\.id$", email)

    def validasi_password(self, password):
        return 8 <= len(password) <= 20 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password)

    def buat_data_baru(self):
        nama = input("Masukkan Nama: ")
        
        # Validasi Email
        while True:
            email = input("Masukkan Email: ")
            if self.validasi_email(email):
                break
            else:
                print("Email yang Anda Masukkan Salah")

        # Validasi Password
        while True:
            password = input("Masukkan Password: ")
            if self.validasi_password(password):
                break
            else:
                print("Password yang Anda masukkan terlalu lemah. Gunakan minimal 1 huruf kapital, huruf kecil, dan angka.")

        self.data['Nama'] = nama
        self.data['Email'] = email
        self.data['Password'] = password
        print("Data berhasil dibuat")

    def simpan_data_ke_file(self):
        nama_file = input("Masukkan nama file tanpa format '.txt': ")
        nama_file += '.txt'

        with open(nama_file, 'a') as file:
            if not self.data['Nama']:
                print("Data saat ini kosong")
                return

            if not file.tell():  # Cek apakah file masih kosong
                file.write("=====================================\n")
                file.write("|Data yang Tersimpan\n")
                file.write("-------------------------------------\n")

            file.write(f"Nama      : {self.data['Nama']}\n")
            file.write(f"Email     : {self.data['Email']}\n")
            file.write(f"Password  : {self.data['Password']}\n")
            file.write("-------------------------------------\n")
            self.data = {
            'Nama': '',
            'Email': '',
            'Password': ''
            }

        print("Berhasil menyimpan data pada file")

def hitung_jumlah_data(nama_file):
    try:
        with open(nama_file, 'r') as file:
            jumlah_data = sum(1 for line in file if re.match(r"[Nama]+[ ]+:+", line))
        print(f"Jumlah data pada file {nama_file}: {jumlah_data}")
    except FileNotFoundError:
        print(f"Tidak Terdapat File dengan Nama {nama_file}")

def main():
    data_pengguna = DataPengguna()

    while True:
        print(f"{'='*50}")
        print("Menu:")
        print("1. Tampilkan Detail Anda")
        print("2. Ubah Nama")
        print("3. Jumlah Data pada File")
        print("4. Simpan Data pada File")
        print("5. Buat Data Baru")
        print("6. Keluar")
        print(f"{'='*50}")
        pilihan = input("Pilih menu (1-6): ")
        print(f"{'='*50}")
        match pilihan:
            case '1':
                data_pengguna.tampilkan_detail()
            case '2':
                data_pengguna.ubah_nama()
            case '3':
                nama_file = input("Masukkan nama file tanpa format '.txt': ")
                nama_file += '.txt'
                hitung_jumlah_data(nama_file)
            case '4':
                data_pengguna.simpan_data_ke_file()
            case '5':
                data_pengguna.buat_data_baru()
            case '6':
                print("Sampai Jumpa Lagi")
                print(f"{'='*50}")
                break
            case _:
                print("Pilihan tidak valid. Silakan pilih menu (1-6)")

if __name__ == "__main__":
    main()
