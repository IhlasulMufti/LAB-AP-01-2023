class Human:
    def __init__(self,name,position) -> None:
        self.name = name
        self.__position = position
        self._speed = 1

    def setPosition(self,position):
        self.__position = position

    def setSpeed(self,speed):
        self._speed = speed

    def getPosition(self):
        return self.__position

    def getSpeed(self):
        return self._speed

    def movement(self, arah):
        for tujuan in arah:
            if str(tujuan).capitalize() == "L":
                new_position = self.getPosition() - self.getSpeed()
                self.setPosition(new_position)

            elif str(tujuan).capitalize() == "R":
                new_position = self.getPosition() + self.getSpeed()
                self.setPosition(new_position)
        

class Hero(Human):
    def __init__(self, name,position) -> None:
        super().__init__(name,position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self.setSpeed(3)

    def setPower(self,power):
        self._power = power
    def getPower(self):
        return self._power
    
    def setHealth(self,health):
        self._health = health
    def getHealth(self):
        return self._health
    
    def setArmor(self,armor):
        self._armor = armor
    def getArmor(self):
        return self._armor

    def attack(self,target):
        damage = target.getHealth() - self._power
        target.setHealth(damage)

class Warrior(Hero):
    def __init__(self, name,position) -> None:
        super().__init__(name,position)
        self.setPower(26)
        self.setArmor(30)
        self.tipe = "Warrior"
    
    def special(self,target):
        self.setArmor(45)
        self.setPower(32)
        self.attack(target)

class Assassin(Hero):
    def __init__(self, name,position) -> None:
        super().__init__(name,position)
        self.setPower(35)
        self.setSpeed(4)
        self.tipe = "Assassin"

    def special(self,target):
        self.setSpeed(7)
        self.setPower(42)
        self.attack(target)

class Support(Hero):
    def __init__(self, name,position) -> None:
        super().__init__(name,position)
        self.setHealth(500)
        self.setArmor(8)
        self.setSpeed(4)
        self.tipe = "Support"

    def special(self,target):
        self.setSpeed(6)
        target.setHealth(target.getHealth()+150)

def print_all_stats(obj,warna):
    print("="*50)
    for attribute, value in vars(obj).items():
        print(f"{warna}{attribute}: {value}")


# Contoh penggunaan oop made by Yusran Mazidan
# nama_player = input("\033[0mMasukkan Nama Player : ")
# nama_musuh = input("Masukkan Nama Target : ")
# while True:
#     print("\033[0m","="*50)
#     print("Masukkan Role Player")
#     print("1. Warrior")
#     print("2. Assassin")
#     print("3. Support")
#     role = int(input("Masukkan Pilihan : "))
#     match role:
#         case 1:
#             player = Warrior(nama_player)
#             break
#         case 2:
#             player = Assassin(nama_player)
#             break
#         case 3:
#             player = Support(nama_player)
#             break
#         case _:
#             print("Harap Masukkan Role Yang Benar!")
#             continue
# print("="*50)

# while True:
#     print("\033[0m"+("="*50))
#     print("Masukkan Role Target")
#     print("1. Warrior")
#     print("2. Assassin")
#     print("3. Support")
#     role = int(input("Masukkan Pilihan : "))
#     match role:
#         case 1:
#             musuh = Warrior(nama_musuh)
#             break
#         case 2:
#             musuh = Assassin(nama_musuh)
#             break
#         case 3:
#             musuh = Support(nama_musuh)
#             break
#         case _:
#             print("Harap Masukkan Role Yang Benar!")
#             continue
# print("="*50)

# while True:
#     print("\033[0m"+("="*50))
#     print("1. Munculkan Stat")
#     print("2. Munculkan Stat Target")
#     print("3. Attack Target")
#     print("4. Skill")
#     print("5. Gerak")
#     print("6. Keluar")
#     pilihan = int(input("Masukkan Pilihan : "))
#     match pilihan:
#         case 1:
#             print_all_stats(player,"\033[32m")
#         case 2:
#             print_all_stats(musuh,"\033[31m")
#         case 3:
#             player.attack(musuh)
#         case 4:
#             player.special(musuh)
#         case 5:
#             arah = input("\033[0mL atau R : ")
#             player.movement(arah)
#         case 6:
#             print("\033[0m","="*50)
#             print(f"{' '*30}GAME OVER")
#             print("="*50)
#             break