class Human:
    def __init__ (self, name, position = 0, speed = 1):
        self.name = name
        self.__position = position
        self._speed = speed
        
    def movement (self, arah):
        for i in arah:
            if i == "R":
                self.__position += self._speed
            elif i == "L":
                self.__position -= self._speed

    def set_position (self, nilai):
        self.__position = nilai
    def get_position (self):
        return self.__position
    
    def set_speed (self, nilai):
        self._speed = nilai
    def get_speed (self):
        return self._speed

class Hero(Human):
    def __init__ (self, name, position = 0, power = 15, health = 400, armor = 15, speed = 3):
        super().__init__ (name, position, speed)
        self._power = power
        self._health = health
        self._armor = armor
        
    def attack (self, target):
        target._health -= self._power
        
    def set_power (self, power):
        self._power = power
    def get_power (self):
        return self._power
    
    def set_health (self, health):
        self._health = health
    def get_health (self):
        return self._health
    
    def set_armor (self, armor):
        self._armor = armor
    def get_armor (self):
        return self._armor
    
class Warrior(Hero):
    def __init__ (self, name, position = 0, power = 26, health = 400, armor = 30, speed = 3):
        super().__init__ (name, position, power, health, armor, speed)
        
    def special (self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power
        
class Assassin(Hero):
    def __init__ (self, name, position = 0, power = 35, health = 400, armor = 40, speed = 4):
        super().__init__ (name, position, power, health, armor, speed)
        
    def special (self, target):
        self._speed = 7
        self._power = 42
        target._health -= self._power

class Support(Hero):
    def __init__ (self, name, position = 0, power = 45, health = 500, armor = 8, speed = 4):
        super().__init__ (name, position, power, health, armor, speed)
        
    def special (self, target):
        self._speed = 6
        target._health += 150