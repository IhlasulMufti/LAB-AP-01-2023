def menghitung_pasangan(angka):
    count_dict = {}
    duplikat = []

    for num in angka:
        if num in count_dict:
            count_dict[num] += 1
            if count_dict[num] % 2 == 0:
                duplikat.append(num)
        else:
            count_dict[num] = 1

    return duplikat

array_1 = input("Input array ke-1: ").split()
array_2 = input("Masukkan array ke-2: ").split()

duplikat = menghitung_pasangan(array_1 + array_2)

if len(duplikat) > 0:
    print(f"Terdapat {len(duplikat)} pasang angka duplikat, yaitu: ({', '.join(map(str, duplikat))})")
else:
    print("Tidak ada duplikat ditemukan")


