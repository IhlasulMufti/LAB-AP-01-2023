def penggabungan(s1,s2):
    s3 = ""
    i = 0

    while i < len(s1) and i < len(s2):
        s3 += s1[i] + s2[i] 
        i += 1
    s3 += s1[i::] + s2[i::] 
    print(s3)

s1 =input("Masukkan Kalimat Pertama ")
s2 = input("Masukkan Kalimat Kedua ")[::-1]
penggabungan(s1,s2)
    