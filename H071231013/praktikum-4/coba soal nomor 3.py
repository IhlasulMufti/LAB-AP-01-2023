'''
def maksimum(*args):
    # Mengecek apakah daftar kosong
    if not args:
        raise ValueError("Daftar kosong")

    # Menginisialisasi nilai terbesar dengan nilai pertama dalam daftar
    max_val = args[0]

    # Membandingkan setiap elemen dalam daftar dengan nilai terbesar
    for num in args:
        if num > max_val:
            max_val = num

    return max_val

# Test Case 1
print(maksimum(1, 2, 4, 6, 9, 3, 1, 9, 10))  # Output yang diharapkan: 10

# Test Case 2
print(maksimum(0, 1, 90, 430, 23, 212, 34))  # Output yang diharapkan: 430
'''

'''
def maksimum(*args):
    try:
        # Mengecek apakah daftar kosong
        if not args:
            raise ValueError("Daftar kosong")

        # Menginisialisasi nilai terbesar dengan nilai pertama dalam daftar
        max_val = args[0]

        # Membandingkan setiap elemen dalam daftar dengan nilai terbesar
        for num in args:
            if num > max_val:
                max_val = num

        return max_val

    except ValueError as e:
        return str(e)

try:
    # Meminta input dari pengguna
    input_nums = input("Masukkan angka-angka dipisahkan oleh spasi: ")
    
    # Mengubah input pengguna menjadi daftar angka
    angka = [int(x) for x in input_nums.split()]

    # Memanggil fungsi maksimum dengan daftar angka sebagai argumen
    hasil = maksimum(*angka)

    # Mencetak hasil
    print("Nilai maksimum:", hasil)
except Exception as e:
    print(f'Terjadi kesalahan karena {e}')
'''

def maksimum(*args):
    # Mengecek apakah daftar kosong
    if not args:
        raise ValueError("Daftar kosong")

    # Menginisialisasi nilai terbesar dengan nilai pertama dalam daftar
    max_val = args[0]

    # Membandingkan setiap elemen dalam daftar dengan nilai terbesar
    for num in args:
        if num > max_val:
            max_val = num

    return max_val

# Meminta input dari pengguna
input_nums = input("Masukkan angka-angka dipisahkan oleh spasi: ")
    
# Mengubah input pengguna menjadi daftar angka
angka = [int(x) for x in input_nums.split()]

# Memanggil fungsi maksimum dengan daftar angka sebagai argumen
hasil = maksimum(*angka)

# Mencetak hasil
print("Nilai maksimum:", hasil)