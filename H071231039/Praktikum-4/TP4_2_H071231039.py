def palindrom(kata: str) -> str:
    kata = kata
    if kata == kata[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"

hasil = palindrom(input())
print(hasil)
