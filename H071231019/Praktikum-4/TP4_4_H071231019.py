def catAndMouse(catA, catB, mosC):
    jarak_catA = catA - mosC if catA > mosC else mosC - catA
    jarak_catB = catB - mosC if catB > mosC else mosC - catB
    # jarak_catA=abs(catA-mosC)
    # jarak_catB=abs(catB-mosC)

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

# Test Case 1
# print(catAndMouse(catA=16, catB=24, mosC=15))  # Cat A

# Test Case 2
# print(catAndMouse(catA=20, catB=10, mosC=15))  # Mouse C
