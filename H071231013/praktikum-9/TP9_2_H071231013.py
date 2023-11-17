class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk): # menginisialisasi atribut-atribut dari objek yang dibuat dari class Mahasiswa
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        print("Informasi Mahasiswa:")
        print(f"Nama: {self.nama}") # untuk menyisipkan nilai atribut nama dari objek ke dalam string yang akan dicetak.
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"IPK: {self.ipk}")

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Cukup"
        else:
            return "Kurang"

nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
jurusan = input("Masukkan jurusan: ")
ipk = float(input("Masukkan IPK: "))

# Membuat objek Mahasiswa dari input pengguna
mahasiswa_input = Mahasiswa(nama, nim, jurusan, ipk)

# Menampilkan informasi dan predikat
mahasiswa_input.tampilkan_info()
print("Predikat:", mahasiswa_input.hitung_predikat())