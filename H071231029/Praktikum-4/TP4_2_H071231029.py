def palindrom(kata):
    kata = kata.lower()
    
    if kata == kata[::-1]:
        return print ("Palindrom")
    return print(" Bukan Palindrom")
''' contoh 1 '''
kata = input()
palindrom(kata)
kata = input()
''' contoh  2''' 
palindrom(kata)


# def palindrom(kata):
#     kata = kata.lower()
#     Miskha = len(kata)
    
#     for i in range(Miskha//2):
#         if kata[i] != kata [Miskha-i -1]:
#             return print("bukan palindrom")
#         return print("Palindrom")
        


# kata =input()
# palindrom(kata)





