class Human:
    def __init__(self, name, pos_x=0,speed=1):
        self.name = name
        self.__position = pos_x
        self._speed = speed

    def movement(self, direction): 
        for i in direction:
            if i == "R":
                self.__position += self._speed
            elif i == "L":
                self.__position -= self._speed

    def set_speed(self, speed):
        self._speed = speed 

    def get_speed(self):
        return self._speed
    
    def set_position(self,pox_x):
        self.__position = pox_x

    def get_position(self):
        return self.__position

class Hero(Human):
    def __init__(self, name, pos_x=0):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target.set_health(target.get_health() - self._power)

    def set_power(self, power):
        self._power = power

    def get_power(self):
        return self._power

    def set_health(self, health):
        self._health = health

    def get_health(self):
        return self._health

    def set_armor(self, armor):
        self._armor = armor

    def get_armor(self):
        return self._armor

class Warrior(Hero):
    def __init__(self, name, pos_x=0):
        super().__init__(name, pos_x)
        self.set_power(26)
        self.set_armor(30)

    def special(self, target):
        self.set_armor(45)
        self.set_power(32)
        target.set_health(target.get_health() - self.get_power())

class Assassin(Hero):
    def __init__(self, name, pos_x=0):
        super().__init__(name, pos_x)
        self.set_power(35)
        self.set_speed(4)

    def special(self, target):
        self.set_speed(7)
        self.set_power(42)
        target.set_health(target.get_health() - self.get_power())

class Support(Hero):
    def __init__(self, name, pos_x=0):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self.set_speed(4)

    def special(self, target):
        self.set_speed(6)
        target.set_health(target.get_health() + 150)

  