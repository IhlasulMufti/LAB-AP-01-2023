def cari_duplikat():
    data1 = set(map(int, input('Masukkan array 1 : ').split()))
    data2 = set(map(int, input('Masukkan array 2 : ').split()))

    duplikat = tuple(data1 & data2)
    jumlah = len(duplikat) 

    if jumlah == 0:
        print("Tidak ada duplikasi ditemukan.")
    elif jumlah ==1:
        print(f"Terdapat {jumlah} buah duplikat yaitu ({duplikat[0]})")
    else:
        print(f"Terdapat {jumlah} buah duplikat yaitu {duplikat}")

    return (duplikat, jumlah)
cari_duplikat()