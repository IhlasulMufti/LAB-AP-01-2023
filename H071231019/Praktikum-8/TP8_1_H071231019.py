import re
def pols(pola,input):
    print(bool(re.match(pola,input)))
    
pola = r"^[A-Za-z02468]{40}[13579\s]{5}$"
input = input("Masukkan input: ")
pols(pola,input)