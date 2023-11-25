from TP9_1A_H071231064 import Warrior,Assassin,Support

warrior = Warrior("bambang",10)
assassin = Assassin("joko",25)
support = Support("udin",30)
# sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.getHealth())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())


# TODO mengubah movement berdasarkan string inputan
print(f"Warrior (posisi) : {warrior.getPosition()}")
warrior.movement('rrlluar')
print(f"Warrior (posisi) : {warrior.getPosition()}")
# print(f"Warrior (posisi) setelah: {warrior.movement('r')}")