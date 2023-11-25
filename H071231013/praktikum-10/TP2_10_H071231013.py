from abc import ABC, abstractmethod
# abc: kelas dasar untuk kelas abstrak
# abstracmethod: dekorator yang digunakan untuk menandai metode sebagai metode abstrak.

# Abstract class
class Animal(ABC): # definisi kelas abstrak Animal yang secara mencolok diwariskan dari ABC.
    def __init__(self, name):
        self._name = name

    def get_name(self): # metode yang mengembalikan nilai atribut self._name.
        return self._name
    
    @abstractmethod #blue print 
    # dekorator yang menandai metode make_sound() sebagai metode abstrak yang harus diimplementasikan oleh kelas turunannya.
    def make_sound(self):
        pass
   
# Inheritance
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self._name = name

    def make_sound(self): #penggunaan abstrak method
        return "Woof!"


# Inheritance
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self._name = name

    def make_sound(self): #penggunaan abstrak method
        return "Meow!"

# Inheritance
class Parrot(Animal):
    def __init__(self, name):
        super().__init__(name)
        self._name = name
        
    def make_sound(self): #penggunaan abstrak method
        return "Squawk!"

# Polymorphism
def animal_sound(animal): # fungsi yang mengambil objek animal dan memanggil metode make_sound() pada objek tersebut untuk mengeluarkan suara hewan.
    return animal.make_sound()

# Encapsulation
dog = Dog("Buddy")
cat = Cat("Whiskers")
parrot = Parrot("Polly")

# Polymorphism
print(f"{dog.get_name()} says: {animal_sound(dog)}") # pemanggilan fungsi animal_sound() dengan objek dari kelas Dog.
print(f"{cat.get_name()} says: {animal_sound(cat)}")
print(f"{parrot.get_name()} says: {animal_sound(parrot)}")
