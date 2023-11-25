from hero import Warrior, Assassin, Support

warrior = Warrior("Alucard", position=10)
assassin = Assassin("Lancelot", position=25)
support = Support("Estes", position=30)

print("Before:", warrior.getPosisi())
warrior.movement('RRLLLLLLLLLLRLRRLRLRLRLRLLRLRLRLRLRLRLRLRLLRLRLRLRLRLRLR')
print("After:", warrior.getPosisi())

print("Health (before):", warrior.getHealth())
assassin.attack(warrior)

print("Health (after):", warrior.getHealth())
print("-" * 50)


print("Warrior (health):", warrior.getHealth())
print("Support (speed):", support.getSpeed())
support.special(warrior)

print("Warrior (health):", warrior.getHealth())
print("Support (speed):", support.getSpeed())
print("-" * 50)
    