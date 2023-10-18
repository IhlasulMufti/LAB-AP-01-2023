def anagrams(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    
    if len(word1) != len(word2):
        return False

    
    jumlah_huruf = {}
    for karakter in word1:
        if karakter in jumlah_huruf:
            jumlah_huruf[karakter] += 1
        else:
            jumlah_huruf[karakter] = 1

    
    for karakter in word2:
        if karakter in jumlah_huruf:
            jumlah_huruf[karakter] -= 1
        else:
            return False  

    
    for count in jumlah_huruf.values():
        if count != 0:
            return False

    return True


word1 = input("Masukkan kata pertama: ")
word2 = input("Masukkan kata kedua: ")

print(anagrams(word1,word2))
