def gabungkata(s1, s2):
    result = ""
    i, j = 0, len(s2) - 1

    while i < len(s1) and j >= 0:
        result += s1[i] + s2[j]
        i += 1
        j -= 1

    result += s1[i:] + s2[:j+1]
    
    return result

kata1 = input('Masukkan kata pertama: ')
kata2 = input('Masukkan kata kedua: ')
print(gabungkata(kata1, kata2))

