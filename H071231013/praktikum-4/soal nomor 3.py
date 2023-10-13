def maksimum(*args):  # sebuah fungsi yang menerima jumlah argumen yang tidak terbatas, kemudian akan mengembalikan nilai terbesar dari argumen tersebut
             # * untuk menandakan bahwa kita akan menerima beberapa argumen dalam bentuk tuple

    # Mengecek apakah daftar kosong

    if not args: # digunakan untuk memeriksa apakah daftar args kosong atau tidak.  jika daftar args kosong(tidak ada argumen yang diberikan saat memanggil fungsi),
    # kondisi if not args akan bernilai true
        raise ValueError("Daftar kosong") # akan di jalankan untuk menghentikan eksekusi program dan menampilkan pesan error ()"Daftar kosong").  jika daftar args tidak kosong,
        # kondisi if not args akan bernilai true

    # Menginisialisasi nilai terbesar dengan nilai pertama dalam daftar
    max_val = args[0] # menginisialisasi variabel max_val dengan nilai pertama dalam daftar args.  ini dilakukan untuk memastikan bahwa ada nilai awal yang dapat dibandingkan

    # Membandingkan setiap elemen dalam daftar dengan nilai terbesar
    for num in args: # untuk melakukan pengulangan pada setiap elemen dalam daftar 'args'
        if num > max_val: # untuk membandingkan nilai num dengan max_val diperbarui dengan num, setelah selesai max_val akan berisi nilai terbesar dalam daftar args
            max_val = num # untuk memperbarui nilai terbesar max_val jika ditemukan elemen yang lebih besar dalam daftar
                          # jika nilai num lebih besar dari max_val akan diperbarui menjadi num
    return max_val # untuk mengembalikan nilai terbesar max_val setelah dilakukan perbandingan pada setiap elemen dalam daftar

# Meminta input dari pengguna
input_nums = input("Masukkan angka-angka dipisahkan oleh spasi: ") # untuk menyimpan input pengguna dalam bentuk string

# Mengubah input pengguna menjadi daftar angka
angka = [int(x) for x in input_nums.split()] # 

# Memanggil fungsi maksimum dengan daftar angka sebagai argumen
hasil = maksimum(*angka)

# Mencetak hasil
print("Nilai maksimum:", hasil)