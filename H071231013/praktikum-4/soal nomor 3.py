def maksimum(*args):

    if not args:

        raise ValueError("Daftar kosong")

    max_val = args[0]

    for num in args:
        if num > max_val:
            max_val = num

    return max_val

input_nums = input("Masukkan angka-angka dipisahkan oleh spasi: ")

angka = [int(x) for x in input_nums.split()]

hasil = maksimum(*angka)

print("Nilai maksimum:", hasil)