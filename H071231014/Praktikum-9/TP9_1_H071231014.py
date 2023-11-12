from hero import Warrior, Assassin, Support

warrior = Warrior("bambang", pos_x=10)
assassin = Assassin("joko", pos_x=25)
support = Support("udin",pos_x=30)

print("health (before)", warrior.get_health())
assassin.attack(warrior)

print("health (after)", warrior.get_health())
print("-"*20)

print("Warrior (health)", warrior.get_health())
print("Support (speed) : ",support.get_speed())
support.special(warrior)

print("Warrior (health)", warrior.get_health())
print("Support (speed): ",support.get_speed())

print("before:",support.get_position())
support.movement("RR")
print("after :",support.get_position())