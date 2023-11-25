class Mahasiswa:

    def __init__(self,name,nim,jurusan,ipk):

        self.name = name
        self.NIM = nim
        self.jurusan = jurusan
        self.IPK = ipk

    def tampilkan_info(self):
        print(f"Nama Mahasiswa : {self.name}\nNIM : {self.NIM}\nJurusan : {self.jurusan}\nIPK : {self.IPK} \n{'='*50}")


    def Hitung_Predikat(self):
        if self.IPK >= 3.5 :
            print("CUMLAUDE ") 
        elif self.IPK >= 3.0:
            print("Sangat Memuaskan")
        elif self.IPK >= 2.5:
            print("Memuaskanji")
        elif self.IPK >= 2.0:
            print("Cukuppp")
        else:
            print("Kurang") 
    
        print('='*50)
        


def Pilihan(name,nim,Jurusan,Ipk):
    Variable = Mahasiswa(name, nim, Jurusan, Ipk)

    while True:
            print("Pilih Opsi Berapa Yang anda Inginkan :\n1.Tampilkan Informasi\n2.Hitung Predikat\n3.Keluar")
            opsi = int(input("Pilih opsi : "))
            print('='*50)

            if opsi == 3:
                print("Selamat Tinggal My Darlinggg")
                exit()
            elif opsi == 1  or opsi == 2:
                    if opsi == 1:
                        Variable.tampilkan_info()
                        Pilihan(name,nim,Jurusan,Ipk)

                    elif opsi == 2:
                        Variable.Hitung_Predikat()
                        Pilihan(name,nim,Jurusan,Ipk)
            else:
                print("Mohon Masukkan Angka Yang Benar")
                
Nama = input("Masukkan nama : ")
Nim = input("Masukkan NIM : ")
Jurusan = input("Masukkan jurusan : ")
while True:
    try:
        Ipk = float(input("Masukkan ipk : "))
        break
    except:
        print("Mohon masukkan angka desimal ")

print('='*50)
Pilihan(Nama, Nim, Jurusan, Ipk)
