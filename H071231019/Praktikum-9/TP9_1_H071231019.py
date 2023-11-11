from hero import Warrior, Assassin, Support
warrior = Warrior("bambang", position=10)
assassin = Assassin("joko", position=25)
support = Support("udin",position=30)

# posisi sebelum dan setelah
print(("posisi sebelum"), assassin.get_position())
assassin.movement("RR")
print("posisi setelah", assassin.get_position())

# sebelum
print("health (before)", warrior.get_health())
assassin.attack(warrior)

# sesudah
print("health (after)", warrior.get_health())
print("-"*10)

# sebelum
print("Warrior (health)", warrior.get_health())
print("Support (speed) : ",support.get_speed())
support.special(warrior)

# sesudah
print("Warrior (health)", warrior.get_health())
print("Support (speed): ",support.get_speed())