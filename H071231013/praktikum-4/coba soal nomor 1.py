def stringPermutation(kata):
    try:
        if len(kata) <= 1:
            return kata

        hasil_permutasi = []
        for i in range(len(kata)):
            kata = kata[-1:] + kata[:-1]  
            hasil_permutasi.append(kata)

        return ' | '.join(hasil_permutasi) + ' |'

    except TypeError as msg:
        return f'Terjadi kesalahan karena {msg}'

print("Test Case 1")
ts1 = stringPermutation(input())
print(ts1) 

print("Test Case 2")
ts2 = stringPermutation(input())
print(ts2)


def stringPermutation(kata):
    try:
        if len(kata) <= 1:
            return kata

        hasil_permutasi = []
        for i in range(len(kata)):
            kata = kata[-1:] + kata[:-1]  
            hasil_permutasi.append(kata)

        return ' | '.join(hasil_permutasi) + ' |'

    except TypeError as msg:
        return f'Terjadi kesalahan karena {msg}'

''' Test Case 1 '''
ts1 = stringPermutation("Mobil")
print(ts1) 

''' Test Case 2 '''
ts2 = stringPermutation("Ayam")
print(ts2)