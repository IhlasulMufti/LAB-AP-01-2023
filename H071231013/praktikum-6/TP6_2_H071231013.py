A = input("Input array ke-1 (pisahkan angka dengan spasi): ").split()
B = input("Input array ke-2 (pisahkan angka dengan spasi): ").split()

A = {int(x) for x in A}
B = {int(x) for x in B}

duplikat = list(A & B)

if len(duplikat) > 0:
    print(f"Terdapat {len(duplikat)} buah duplikat yaitu {tuple(duplikat)}")
else:
    print("Tidak ada duplikasi ditemukan.")