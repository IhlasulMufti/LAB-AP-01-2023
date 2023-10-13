def stringPermutation(kata): # mendefnisikan sebuah fungsi yaitu stringPermutation,  untuk menerima satu inputan yaitu kata, string yang akan dipermutasi
    try: # untuk menangani kemungkinan terjadinya error saat menjalankan program
        if len(kata) <= 1: # untuk menangani jika panjang kata yang diberikan kurang dari atau sama dengan 1
            return kata # saat panjang kata yang diberikan kurang dari atau sama dengan 1. contoh: saat saya memasukkan kata 'a' maka panjangnya adalah 1 dan tidak perlu dilakukan
                        # permutasi, karena fungsi stringPermutation langsung mengembalikan kata itu melalui RETURN KATA
        hasil_permutasi = [] # untuk menyimpan semua hasil permutasi dari kata yang diberikan  hasil_permutasi itu sebuah list kosong yang akan diisi dengan setiap hasil
                             # permutasi dari kata pada setiap iterasi perulangan 
        for i in range(len(kata)): #
            kata = kata[-1:] + kata[:-1] # untuk melakukan permutasi pada kata yang diberikan   kata[-1:]: untuk mendapatkan karakter terakhir dari kata, kalau kata[-1:]: untuk
                                         # mendapatkan semua karakter kecuali karakter terakhir
            hasil_permutasi.append(kata) # untuk menambahkan nilai dari variabel kata ke dalam list hasil_permutasi,  dalam setiap melakukan perulangan, nilai kata yang telah
# berubah akan ditambahkan ke dalam list hasil_permutasi menggunakan append,dengan menggunakan append setiap hasil permutasi dari kata yang diberikan akan ditambahkan ke dalam
# list hasil_permutasi secara berurutan

        return ' | '.join(hasil_permutasi) + ' |' # semua hasil permutasi dalam list hasil_permutasi akan digabungkan menjadi sebuah string dengan pemisah "|" (garis vertikal) di
                                                  # antara setiap permutasi.

    except TypeError as msg: # menangkap kesalahan tipe yang terjadi saat menjalankan kode di dalam blok try,  jika terjadi TypeError maka pesan kesalahan yang dihasilkan akan
                             # disimpan dalam variabel ms
        return f'Terjadi kesalahan karena {msg}' # mengembalikan sebuah string yang berisi pesan kesalahan yang dihasilkan oleh TypeError dalam bentuk format string(f-string)

print("Test Case 1")
ts1 = stringPermutation(input())
print(ts1) 

print("Test Case 2")
ts2 = stringPermutation(input())
print(ts2)