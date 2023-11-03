def tigahuruf(isi):
    hasil= ''
    if len(kata) < 3:
        print('Kata terlalu pendek')
    elif len(kata) % 2 == 0:
        indekstengah = len(kata) // 2
        hasil = kata[0] + kata[indekstengah-1] + kata[indekstengah] + kata[-1]
        return hasil
    else:
        indekstengah = len(kata) // 2
        hasil = kata[0] + kata[indekstengah] + kata[-1]
        return hasil

kata = input('Masukkan Kata: ')
print('Hasilnya adalah:',tigahuruf(kata))