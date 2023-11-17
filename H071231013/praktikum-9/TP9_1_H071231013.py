from Hero import Warrior, Assassin, Support

warrior = Warrior("Bambang", pos_x=10)
assassin = Assassin("Joko", pos_x=25)
support = Support("Udin", pos_x=30)

# sebelum 
print("Health (before):", warrior.get_health())
assassin.attack(warrior)
# sesudah
print("Health (after):", warrior.get_health())
print("-" * 10)
# sebelum
print("Warrior (health):", warrior.get_health())
print("Support (speed):", support.get_speed)
support.special(warrior)
# sesudah
print("Warrior (health):", warrior.get_health())
print("Support (speed):", support.get_speed)