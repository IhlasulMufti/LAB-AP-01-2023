def gabung(kata):
    tengah = len(kata) // 2
    if len(kata) % 2 == 0:
        kata_tengah = kata[tengah-1] + kata[tengah]
    else:
        kata_tengah = kata[tengah]
    return kata[0] + kata_tengah + kata[-1]

kata = input()
print(gabung(kata))