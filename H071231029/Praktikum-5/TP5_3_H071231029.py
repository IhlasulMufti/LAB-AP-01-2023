kata_1 = input('Masukkan kata pertama: ').lower()
kata_2 = input('Masukkan kata kedua: ').lower()

if len(kata_1) == len(kata_2):
    daftar_1 = []    
    daftar_2 = []

    for huruf in kata_1:

        daftar_1.append(huruf)
    for huruf in kata_2:
        daftar_2.append(huruf)

    hasil = True
    for i in daftar_1:
        if i not in daftar_2:
            hasil = False
            break

    if hasil:
        print(True)
    else:
        print(False)
else:
    print(False)

''' RINGKAS'''
# kata_satu = input("Masukkan kata 1 : ").lower().replace(" ","")
# kata_dua = input("Masukkan kata 2 : ").lower().replace(" ","")
# if len(kata_satu) == len(kata_dua) and sorted(kata_satu) == sorted(kata_satu):
#     print(True)
# else:
#     print(False)
