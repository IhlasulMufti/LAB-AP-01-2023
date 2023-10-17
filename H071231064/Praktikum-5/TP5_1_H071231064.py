def gabung_string(s1, s2):
    hasil = ""
    i = 0
    j = len(s2) - 1
    k = len(s2) - 1

    while i < len(s1) and j >= 0:
        hasil += s1[i] + s2[j]
        i += 1 
        j -= 1

    if(len(s1)>len(s2)):
        hasil += s1[i:]
    else:
        hasil += s2[:j+1]

    return hasil

s1 = input("s1 = ")
s2 = input("s2 = ")
print("Hasil mixed = {}".format(gabung_string(s1,s2)))
