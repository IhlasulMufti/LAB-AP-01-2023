def is_palindrome(word: str) -> str: # memeriksa apakah sebuah kata merupakan palindrom atau bukan, fungsi ini juga menerima sebuah parameter berupa string kata yang akan diperiksa                      
    # fungsi ->: untuk tidak mengubah jenis tipe data variabelnya,misalkan str,akan tetap str

    # Menghapus spasi dan mengubah huruf menjadi huruf kecil

    cleaned_word = "".join(word.split()).lower() # untuk membersihkan kata dari spasi dan mengubah huruf-hurufnya menjadi huruf kecil
                    # "".join(word.split()) : untuk menggabungkan semua kata dalam string menjadi satu tanpa spasi di antara kata kata,
                    # split(): untuk memisahkan kata kata dalam string menjadi list berdasarkan spasi

    # Memeriksa apakah kata adalah palindrom
    if cleaned_word == cleaned_word[::-1]:     # untuk memeriksa apakah kata yang telah dibersihkan dan dikonversi menjadi huruf kecil merupakan sebuah palindrom atau bukan
                       # untuk membalikkan urutan karakter kata yang dibersihkan. 
        return "Palindrom" # untuk mengembalikan nilai "Palindrom" jika yang diberikan oleh pengguna merupakan sebuah palindrom
    else:
        return "Bukan Palindrom"

# Meminta input dari pengguna
input_word = input("Masukkan kata palindrom: ")
hasil = is_palindrome(input_word) # untuk memanggil fungsi is_palindrome dengan argumen input_word, is_palindrome akan memeriksa apakah kata yang dimasukkan palindrom atau bukan
                                  # hasil dari is_palindrome akan disimpan dalam variabel hasil
# mencetak hasil

print(hasil)
hasil = (f'Bukan Palindrom') # untuk menginisialisasi variabel hasil dengan string 'Bukan Palindrom'

# Meminta input dari pengguna
input_word = input("Masukkan kata: ")
hasil = is_palindrome(input_word)

# mencetak hasil

print(hasil)
hasil = (f'Bukan Palindrom')