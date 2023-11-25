class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk) -> None:
        self.nama = nama
        self.__nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def getNim(self):
        return self.__nim
    
    def setNim(self,nim):
        self.__nim = nim

    def tampilkan_info(self):
        print("="*50)
        for attribute, value in vars(self).items():
            print(f"{attribute}: {value}")
        print("="*50)

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif self.ipk >= 3:
            return "Sangat memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2:
            return "Cukup"
        else:
            return "Kurang"

anu = Mahasiswa("Yusran","H071231064","MIPA",3)
anu.tampilkan_info()
print(anu.hitung_predikat())

nama = input("Masukkan Nama Mahasiswa : ")
nim = input("Masukkan Nim Mahasiswa : ")
jurusan = input("Masukkan Jurusan Mahasiswa : ")
ipk = int(input("Masukkan IPK Mahasiswa : "))

mhs = Mahasiswa(nama,'fds',jurusan,ipk)
mhs.setNim(nim)
mhs.tampilkan_info()
print(mhs.hitung_predikat())
