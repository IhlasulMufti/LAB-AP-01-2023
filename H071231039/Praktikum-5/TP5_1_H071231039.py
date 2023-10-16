s1 = input('Masukkan kata pertama: ')
s2 = input('Masukkan kata kedua: ')

result = ""
i, j = 0, len(s2) - 1

while i < len(s1) and j >= 0:
    result += s1[i] + s2[j]
    i += 1
    j -= 1

result += s1[i:] + s2[:j+1]

print(f'Hasilnya adalah: {result}')
