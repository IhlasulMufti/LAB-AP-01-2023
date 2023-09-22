# Menerima tiga input string
input1 = input("Masukkan Input Pertama: ").lower()
input2 = input("Masukkan Input Kedua: ").lower()
input3 = input("Masukkan Input Ketiga: ").lower()

# memeriksa apakah input valid (tidak mengandung spasi)
if ' ' not in input1 and ' ' not in input2 and ' ' not in input3:
    if input1 == "vertebrado":
        if input2 == "ave":
            if input3 == "carnivoro":
                print("aguia")
            elif input3 == "onivoro":
                print("pomba")
            else:
                print("Invalid input")
        elif input2 == "mamifero":
            if input3 == "onivoro":
                print("homem")
            elif input3 == "herbivoro":
                print("vaca")
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    elif input1 == "invertebrado":
        if input2 == "inseto":
            if input3 == "hematofago":
                print("pulga")
            elif input3 == "herbivoro":
                print("lagarta")
            else:
                print("Invalid input")
        elif input2 == "anelideo":
            if input3 == "hematofago":
                print("sanguessuga")
            elif input3 == "onivoro":
                print("minhoca")
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
else:
    print("Invalid input")
