from abc import ABC, abstractmethod
class Laptop:
    def __init__(self, warna, merk, processor, ram, vga):
        self._warna = warna
        self.__merk = merk
        self.__processor = processor
        self.__ram = ram
        self.__vga = vga

    def getWarna(self):
        return self._warna
    def getMerk(self):
        return self.__merk
    def getProcessor(self):
        return self.__processor
    def getRam(self):
        return self.__ram
    def getVga(self):
        return self.__vga

    def setWarna(self, warna):
        self._warna = warna
    def setMerk(self, merk):
        self.__merk = merk
    def setProcessor(self, processor):
        self.__processor = processor
    def setRam(self, ram):
        self.__ram = ram
    def setVga(self, vga):
        self.__vga = vga
        
class Bentuk(ABC):
    @abstractmethod
    def HitungLuas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def HitungLuas(self):
        return self.sisi ** 2

class Segitiga(Bentuk):
    def __init__(self, panjang, alas, tinggi):
        self.panjang = panjang
        self.alas = alas
        self.tinggi = tinggi
    def HitungLuas(self):
        return 1/2 * self.alas * self.tinggi
    
def Hitungluas(Bentuk):
    print(Bentuk.HitungLuas())


laptop1 = Laptop(warna = 'Hitam', merk = 'Lenovo', processor = 'Intel Core i7', ram = '16GB', vga = 'NVIDIA GeForce RTX 3060')
print(f'Saya memiliki laptop berwarna {laptop1.getWarna()}, merek {laptop1.getMerk()}, dengan prosesor {laptop1.getProcessor()}, RAM {laptop1.getRam()}, dan VGA {laptop1.getVga()}.')

jenis_bentuk = input("Masukkan jenis bentuk (Persegi atau Segitiga): ")
if jenis_bentuk.lower() == "persegi":
    sisi = float(input("Masukkan panjang sisi persegi: "))
    bentuk = Persegi(sisi)
elif jenis_bentuk.lower() == "segitiga":
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    bentuk = Segitiga(alas, tinggi)
else:
    print("Jenis bentuk tidak dikenal")

Hitungluas(bentuk)