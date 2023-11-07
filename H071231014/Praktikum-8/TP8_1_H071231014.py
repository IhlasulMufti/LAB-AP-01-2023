# Soal 1 : Mengecek dan memvalidasi sebuah string inputan dari user
import re

def validasi_string(string):
    pola = r'^[a-zA-Z2468]{40}[13579\s]{5}$'
    return re.search(pola, string)
print(bool(validasi_string(input())))