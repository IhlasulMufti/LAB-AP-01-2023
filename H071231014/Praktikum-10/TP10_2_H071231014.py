from abc import ABC,abstractmethod

class Outfit(ABC):
    def __init__(self,model):
        self._model = model

    @abstractmethod
    def warna(self):
        pass
    
    def set_model(self,model):
        self._model = model

    def get_model(self):
        return self._model

class Jilbab(Outfit):
    def __init__(self, model):
        super().__init__(model)

    def warna(self):
        return "hitam"
    
class baju(Outfit):
    def __init__(self, model):
        super().__init__(model)

    def warna(self):
        return "merah muda"

class celana(Outfit):
    def __init__(self, model):
        super().__init__(model)

    def warna(self):
        return "kuning"

def spillWarna(object):
    print(f"{object.warna()}")

atasan = Jilbab("segitiga")
pakaian = baju("tunik")
bawahan = celana("kulot")

print("saya mau keluar jalan-jalan dengan Outfit")
print("warna jilbab:")
spillWarna(atasan)
print("model jilbab:")
print(atasan.get_model())

print("\nwarna baju:")
spillWarna(pakaian)
print("model baju:")
print(pakaian.get_model())

print("\nwarna celana:")
spillWarna(bawahan)
print("model celana:")
print(bawahan.get_model())

