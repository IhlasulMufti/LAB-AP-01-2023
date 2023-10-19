def singkatan(kata):
    panjang_string = len(kata)
    if panjang_string < 3:
        return "Panjang string harus lebih dari 2 karakter."
    if panjang_string%2==0:
        index_tengah = panjang_string // 2
        hasil = kata[0] + kata[index_tengah-1] + kata[index_tengah] + kata[-1]
    else:
        index_tengah = panjang_string // 2
        hasil = kata[0] + kata[index_tengah] + kata[-1]
    return hasil

kata = input("Masukkan string: ")
print(singkatan(kata))
