class Mahasiswa:
    def __init__(self,nama,nim,jurusan,ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan 
        self.__ipk = float(ipk)

    def set_ipk(self,ipk):
        self.__ipk = ipk

    def get_ipk(self):
        return self.__ipk

    def tampilan_info(self):
        print("Nama:",self.nama)
        print("Nim:",self.nim)
        print(f"Jurusan:{self.jurusan}")
        print(f"IPK:{self.__ipk}")

    def hitung_predikat(self):
        if self.__ipk >= 3.5:
            return "Cumlaude"
        elif self.__ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.__ipk >= 2.5:
            return "Memuaskan"
        elif self.__ipk >= 2.0:
            return "Cukup"
        else:
            return "Kurang"
        
nama = input("Nama:")
nim = input("NIM:")
jurusan = input("Jurusan:")
ipk = float(input("IPK:"))

Mahasiswa1 = Mahasiswa(nama,nim,jurusan,ipk)

print("")
Mahasiswa1.tampilan_info()
print("Predikat:",Mahasiswa1.hitung_predikat())