def cariduplikat(ar1, ar2):
    set1 = set(ar1)
    set2 = set(ar2)

    duplikat = set1.intersection(set2)
   
    if len(duplikat) > 0:
        print(f'Terdapat {len(duplikat)} buah duplikat yaitu',duplikat)
    else:
        print('Tidak ada duplikat yang ditemukan')


array1= input('Masukkan array 1: ').split(' ')
array2= input('Masukkan array 2: ').split(' ')
cariduplikat(array1, array2)


