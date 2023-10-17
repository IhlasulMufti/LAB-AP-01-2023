def singkatan(kata):
    panjang_string = len(kata)
    if panjang_string < 3:
        return "Panjang string harus lebih dari 2 karakter."
    index_tengah = panjang_string // 2
    hasil = kata[0] + kata[index_tengah] + kata[-1]
    return hasil

kata = input("Masukkan string: ")
print(singkatan(kata))
