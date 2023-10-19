def gabungan(s1,s2):
    s3 = ""
    panjang = min(len(s1), len(s2))
    s2=s2[::-1]
    for i in range(panjang):
        s3 += s1[i] + s2[i]
    
    s3+= s1[panjang:] + s2[panjang:]
    return s3

s1 = input("Masukan kata pertama : ")
s2 = input("Masukan kata kedua : ")
output=gabungan(s1,s2)
print(output)