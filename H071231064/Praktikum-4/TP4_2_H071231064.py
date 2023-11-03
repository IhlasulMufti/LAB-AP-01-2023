def palindrom(kata:str) -> str:
    kata = kata.lower()
    kata_balik = ""
    for karakter in kata:
        kata_balik = karakter + kata_balik

    if kata_balik == kata:
        return "Palindrome"
    else:
        return "Bukan"
        
kalimat = input("Masukkan Kata : ")
print(palindrom(kalimat))
