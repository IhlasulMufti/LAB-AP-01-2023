array1 =input("Masukkan Array1: ").split()
array1=[int(i)for i in array1] 
array2 =input("Masukkan Array2: ").split()
array2 =[int(i)for i in array2]
array3 = set(array1)&set(array2)

if len(array3) == 1:
    print(f"terdapat {len(array3)} buah duplikat yaitu ({array3})")
elif len(array3) >1:
    array3=tuple(array3)
    print(f"terdapat {len(array3)} buah duplikat yaitu {array3}")
else:
    print("tidak ada duplikasi ditemukan ")