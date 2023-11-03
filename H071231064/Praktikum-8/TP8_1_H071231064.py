import re

inputan = input("Masukkan inputan: ")


pola1 = r'[a-zA-Z02468]'
pola2 = r'[13579\s]'

if len(inputan) == 45 and re.findall(pola1, inputan[:40]) and re.findall(pola2, inputan[40:]):
    print("True")
else:
    print("False")
