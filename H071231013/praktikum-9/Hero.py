class Human:
    def __init__(self, name, pos_x):
        self.name = name
        self.__pos_x = pos_x # Menyimpan nilai pos_x sebagai atribut 
        self._get_speed = 0 #  Menyimpan nilai 0 sebagai atribut _get_speed, yang bersifat protected.

    def movement(self, arah):
        if arah == "L": # untuk mengubah posisi horizontal (pos_x) manusia ke kiri dengan mengurangi nilai dari self.__pos_x menggunakan self.get_speed.
            self.__pos_x -= self.get_speed # mengurangkan nilai dari atribut __pos_x.
        elif arah == "R": #untuk melakukan pengecekan apakah nilai dari arah adalah "R". Jika nilai dari arah adalah "R", maka blok kode di dalam kondisi tersebut akan dieksekusi.
            self.__pos_x += self.get_speed # perintah yang menambahkan nilai dari atribut get_speed pada objek dengan nilai dari atribut __pos_x pada objek tersebut.

    def get_pos_x(self):
        return self.__pos_x

    def set_pos_x(self, pos_x):
        self.__pos_x = pos_x


class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x) # memanggil konstruktor dari superclass atau class induk dari class human
        self._power = 15
        self._health = 400
        self._armor = 15
        self._get_speed = 3

    def get_health(self):
        return self._health
    
    def set_health(self, health):
        self._health = health

    def attack(self, target):
        target.set_health(target.get_health() - self._power)


class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self._armor = 45
        self._power = 32
        self.attack(target)


class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self.get_speed = 4

    def special(self, target):
        self.get_speed = 7
        self._power = 42
        self.attack(target)


class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self.get_speed = 4

    def special(self, target):
        self.get_speed = 6
        target.set_health(target.get_health() + 150)
