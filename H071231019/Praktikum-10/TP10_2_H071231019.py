from abc import ABC, abstractmethod

class MieInstan(ABC):
    def __init__(self, nama, rasa):
        self._nama = nama
        self._rasa = rasa
    
    @abstractmethod
    def tempat_dibeli(self):
        pass

    def display_info(self):
        print(f"Mie Instan {self._nama} rasa {self._rasa}")

    def get_nama(self):
        return self._nama

    def set_nama(self, nama):
        self._nama = nama

    def get_rasa(self):
        return self._rasa

    def set_rasa(self, rasa):
        self._rasa = rasa
        
class Indomie(MieInstan):
    def __init__(self, rasa):
        super().__init__("Indomie", rasa)

    def tempat_dibeli(self):
        return "Dapat dibeli di Indomaret"

class MieSedap(MieInstan):
    def __init__(self, rasa):
        super().__init__("Mie Sedap", rasa)

    def tempat_dibeli(self):
        return "Dapat dibeli di Alfamart"

class MieGelas(MieInstan):
    def __init__(self, rasa):
        super().__init__("Mie Gelas", rasa)

    def tempat_dibeli(self):
        return "Dapat dibeli di Alfamidi atau Kios"

# Polymorphism
def cetak_tempat_dibeli(mie):
    print(mie.tempat_dibeli())

indomie_ayam = Indomie("Ayam Bawang")
mie_sedap_soto = MieSedap("Soto")
mie_gelas_kari = MieGelas("Kari Ayam")

indomie_ayam.display_info()
mie_sedap_soto.display_info()
mie_gelas_kari.display_info()

cetak_tempat_dibeli(indomie_ayam)
cetak_tempat_dibeli(mie_sedap_soto)
cetak_tempat_dibeli(mie_gelas_kari)