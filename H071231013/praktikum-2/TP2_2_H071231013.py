pertama = input(f'Masukkan Input Pertama : ').lower()
kedua = input(f'Masukkan Input Kedua : ').lower()
ketiga = input(f'Masukkan Input Ketiga : ').lower()

if pertama == "vertebrado":
    if kedua == "ave":
        if ketiga == "carnivoro":
            print("aguia")
        elif ketiga == "onivoro":
            print("pomba")
        else:
            print("Invalid input")
    elif kedua == "mamifero":
        if ketiga == "onivoro":
            print("homem")
        elif ketiga == "herbivoro":
            print("vaca")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
elif pertama == "invertebrado":
    if kedua == "inseto":
        if ketiga == "hematofago":
            print("pulga")
        elif ketiga == "herbivoro":
            print("lagarta")
        else:
            print("Invalid input")
    elif kedua == "anelideo":
        if ketiga == "hematofago":
            print("sanguessuga")
        elif ketiga == "onivoro":
            print("minhoca")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
else:
    print("Invalid input")