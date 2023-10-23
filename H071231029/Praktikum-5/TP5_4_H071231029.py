angk = input("Masukkan int: ")
bnykk = []

for i in angk.split("."):
    hurup =str(int(i))
    bnykk.append(hurup)
bnykk =".".join(bnykk)
print(bnykk)
