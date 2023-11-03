def permutasikata(kata):
    for i in range(len(kata)):
        kata = kata[-1] + kata[:-1]
        print(kata, end= '|')

permutasikata(input())

