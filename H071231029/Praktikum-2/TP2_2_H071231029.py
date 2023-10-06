inp1 = input("Masukkan input pertama : ").lower()
inp2 = input("Masukkan input kedua : ").lower()
inp3 = input("Masukkan input ketiga : ").lower()

if inp1 == "vertebrado":
    if inp2 == "ave":
        if inp3 == "cornivoro":
            print("agula")
        elif inp3 == "onivoro":
            print("Pomba")
        else:
            print("Invalid Input")
    elif inp2 == "mamifero":
        if inp3 == "onivoro":
            print("ohem")
        elif inp3 == "herbivoro":
            print("Vaca")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
elif inp1 == "invertebrado":
    if inp2 == "inseto":
        if inp3 == "imatofago":
            print("pulga")
        elif inp3 == "herbivoro":
            print("lagarta")
        else:
            print("Invalid Input")
    elif inp2 == ("anelideo"):
        if inp3 == ("hematofago"):
            print("Saguesugga")
        elif inp3 == ("onivoro"):
            print("minhoca")
        else:
            print("Invalid Input")
    else:
        print("Invalid input")
else:
    print("Invalid Input")

