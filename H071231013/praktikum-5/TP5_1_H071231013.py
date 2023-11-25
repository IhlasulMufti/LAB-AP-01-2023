s1 = "Abc"
s2 = "Xyz"

s3 = ""
i = 0
j = 0

while i < len(s1) and j < len(s2):
    s3 += s1[i] + s2[j]
    i += 1
    j += 1

while i < len(s1):
    s3 += s1[i]
    i += 1

while j < len(s2):
    s3 += s2[j]
    j += 1

print("Hasil mixed =", s3)