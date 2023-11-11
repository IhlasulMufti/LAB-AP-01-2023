class Human:
    def __init__(self, name, position, speed=1):
        self.nama = name
        self.__posisi = position
        self._speed = speed
    
    def movement(self, arah):
        for i in arah:
            if i == 'L':
                self.__posisi = self.__posisi - self._speed
            elif i == 'R':
                self.__posisi = self.__posisi + self._speed

    def setPosisi(self, position):
        self.__posisi = position

    def getPosisi(self):
        return self.__posisi

    def setSpeed(self, speed):
        self._speed = speed

    def getSpeed(self):
        return self._speed

class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target._health = target._health - self._power
        return target._health

    def setPower(self, power):
        self._power = power

    def getPower(self):
        return self._power

    def setHealth(self, health):
        self._health = health

    def getHealth(self):
        return self._health

    def setArmor(self, armor):
        self._armor = armor

    def getArmor(self):
        return self._armor

    def setSpeed(self, speed):
        self._speed = speed

    def getSpeed(self):
        return self._speed

class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health = target._health - self._power

class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self._speed = 7
        self._power = 32
        target._health = target._health - self._power

class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target._health = target._health + 150