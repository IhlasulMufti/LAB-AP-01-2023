class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.__jurusan = jurusan
        self.ipk = ipk

    def getjurusan(self):
        return self.__jurusan
    
    def setjurusan(self,jurusan):
        self.__jurusan = jurusan

    def tampilkan_info(self):
        print('Nama:',self.nama)
        print('NIM:',self.nim)
        print('Jurusan:',self.__jurusan)
        print('IPK:',self.ipk)

    def hitung_predikat(self):
    
        if self.ipk >= 3.5:
            return 'Cumlaude'
        elif self.ipk >= 3.0:
            return 'Sangat Memuaskan'
        elif self.ipk >= 2.5:
            return 'Memuaskan'
        elif self.ipk >= 2.0:
            return 'Cukup'
        else:
            return 'Kurang'

Nama = input("Masukkan Nama Mahasiswa: ")
NIM = input("Masukkan NIM Mahasiswa: ")
Jurusan = input("Masukkan Jurusan Mahasiswa: ")
IPK = float(input("Masukkan IPK Mahasiswa: "))


mahasiswa1 = Mahasiswa(Nama, NIM, Jurusan, IPK)
print('Predikat Mahasiswa:',mahasiswa1.hitung_predikat())
mahasiswa1.tampilkan_info()
