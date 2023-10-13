'''
def is_palindrome(word: str) -> str:
    # Menghapus spasi dan mengubah huruf menjadi huruf kecil
    cleaned_word = "".join(word.split()).lower()

    # Memeriksa apakah kata adalah palindrom
    if cleaned_word == cleaned_word[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"

# Meminta input dari pengguna
input_word = input("Masukkan kata: ")
hasil = is_palindrome(input_word)

# Mencetak hasil
print(hasil)
'''

def is_palindrome(word: str) -> str: # fungsi ->: untuk tidak mengubah jenis tipe data variabelnya,misalkan str,akan tetap str
    # Menghapus spasi dan mengubah huruf menjadi huruf kecil

    cleaned_word = "".join(word.split()).lower()

    # Memeriksa apakah kata adalah palindrom
    if cleaned_word == cleaned_word[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"

# Meminta input dari pengguna

input_word = input("Masukkan kata: ")
hasil = is_palindrome(input_word)

# Mencetak hasil

print(hasil)
hasil = (f'Bukan Palindrom')

# Meminta input dari pengguna

input_word = input("Masukkan kata: ")
hasil = is_palindrome(input_word)

# mencetak hasil

print(hasil)
hasil = (f'Bukan Palindrom')