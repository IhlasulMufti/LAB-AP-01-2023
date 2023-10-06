def cek_palindrom(kata):
    if kata == kata[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"
    
kata = input("Masukkan kata: ")
print(cek_palindrom(kata))