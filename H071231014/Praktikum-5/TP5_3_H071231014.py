def anagram(kata1,kata2):
    kesalahan = 0 
    kata1= kata1.replace(" ","").lower()
    kata2= kata2.replace(" ","").lower()
    
    for karakter in kata1:
        cek1=kata1.count(karakter)
        cek2=kata2.count(karakter)
        if cek1 != cek2:
            kesalahan += 1
    if kesalahan == 0 and len(kata1) == len(kata2):
        return True
    else:
        return False
    
kata1= input("masukan kata pertama:")
kata2= input("masukan kata kedua: ")
print(f"ini adalah anagram {anagram(kata1,kata2)}")


# def anagram(kata1,kata2):
#     ganti1= kata1.replace(" ", "").lower()
#     ganti2= kata2.replace(" ", "").lower()
#     print(sorted(kata1) == sorted(kata2))

# kata1= input("Masukan kata pertama: ")
# kata2= input("Masukan kata kedua: ")
# anagram(kata1,kata2) 

        

