kata = input('Masukkan kata: ').replace(' ','')

if len(kata) < 3:
    print('Kata terlalu pendek')
else:
    indekstengah = len(kata) // 2
    hasil = kata[0] + kata[indekstengah] + kata[-1]
    print(f'Hasilnya adalah: {hasil}')