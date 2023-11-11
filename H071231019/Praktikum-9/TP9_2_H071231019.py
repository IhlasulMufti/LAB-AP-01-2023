class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.name = nama
        self.__nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        print("Nama: ", self.name)
        print("NIM: ", self.__nim)
        print("Jurusan: ", self.jurusan)
        print("IPK: ", self.ipk)

    def set_nim(self, nim):
        self.nim = nim
    def get_nim(self):
        return self.nim

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
        
nama = input("Nama: ")
nim = input("NIM: ")
jurusan = input("Jurusan: ")
ipk = float(input("IPK: "))

mahasiswa1 = Mahasiswa(nama, nim, jurusan, ipk)
print("---------------")
mahasiswa1.tampilkan_info()
print("Predikat:", mahasiswa1.hitung_predikat())