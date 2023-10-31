def input_array():
    array1 = list(map(int,input("Input array ke-1: ").split()))
    array2 = list(map(int,input("Input array ke-2: ").split()))

    input_array=[]
    for i in array1:
        if i in array2 and i not in input_array:
            input_array.append(i)
    return input_array

def program_array():
    duplicate = input_array()
    if len(duplicate)>0:
        print(f"Terdapat {len(duplicate)}, buah duplicate yaitu {tuple(duplicate)}")
    else:
        print("Tidak ada duplicate")

program_array()