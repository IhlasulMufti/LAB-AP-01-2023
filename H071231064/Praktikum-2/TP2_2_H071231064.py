input_pertama = input("Masukkan Input Pertama: ")
input_kedua = input("Masukkan Input Kedua: ")
input_ketiga = input("Masukkan Input Ketiga: ")

match (input_pertama, input_kedua, input_ketiga):
    case ("vertebrado", "ave", "carnivoro"):
        print("agula")
    case ("vertebrado", "ave", "onivoro"):
        print("pomba")
    case ("vertebrado", "mamifero", "onivoro"):
        print("homem")
    case ("vertebrado", "mamifero", "herbivoro"):
        print("vaca")
    case ("invertebrado", "inseto", "hematofago"):
        print("Pulga")
    case ("invertebrado", "inseto", "herbivoro"):
        print("Lagarta")
    case ("invertebrado", "anelideo", "hematofago"):
        print("Sanguessuga")
    case ("invertebrado", "anelideo", "onivoro"):
        print("Minhoca")
    case _:
        print("Kombinasi input tidak dikenali")