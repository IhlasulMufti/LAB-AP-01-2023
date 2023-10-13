def catAndMouse(catA, catB, mosC):
    jarak_catA = catA - mosC if catA > mosC else mosC - catA
    jarak_catB = catB - mosC if catB > mosC else mosC - catB

    if jarak_catA < jarak_catB:
        return "Cat A"
    elif jarak_catB < jarak_catA:
        return "Cat B"
    else:
        return "Mouse C"

catA=int(input("Kucing A: "))
catB=int(input("Kucing B: "))
mosC=int(input("Tikus: "))
print(catAndMouse(catA, catB, mosC))