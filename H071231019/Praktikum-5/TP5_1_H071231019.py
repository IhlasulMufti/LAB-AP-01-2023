def gabung_str(s1, s2):
    s3 = ''
    len_s1, len_s2 = len(s1), len(s2)
    s2=s2[::-1] 
    for i in range(max(len_s1, len_s2)): 
        if i < len_s1: 
            s3 += s1[i]  
        if i < len_s2:
            s3 += s2[i]
    return s3
s1 = input("Masukkan kata 1: ")
s2 = input("Masukkan kata 2: ")
print(gabung_str(s1, s2))