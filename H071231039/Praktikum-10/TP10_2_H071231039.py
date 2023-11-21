from abc import ABC, abstractmethod


class Mobil:
    def __init__(self, warna, merk):
        self._warna = warna
        self.__merk = merk
    
    def getWarna(self):
        return self._warna
    def getMerk(self):
        return self.__merk
    def setWarna(self, warna):
        self._warna = warna
    def setMerk(self, merk):
        self.__merk = merk
        

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

    
mobil1 = Mobil(warna = 'Hijau', merk = 'Toyota')
print(f'Saya memiliki mobil berwarna {mobil1.getWarna()} merek {mobil1.getMerk()}')

luaspersegi = Persegi(sisi = 4)
luassegitiga = Segitiga(panjang= 5, alas = 4, tinggi = 6)

Hitungluas(luaspersegi)
Hitungluas(luassegitiga)



