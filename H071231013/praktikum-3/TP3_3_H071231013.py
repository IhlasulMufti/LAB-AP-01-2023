while True: # loop tak terbatas yang akan terus berjalan hingga terjadi EOFError (pencetakan Ctrl+D atau Ctrl+Z).
    try: # blok percobaan yang digunakan untuk menangani exception yang mungkin terjadi dalam blok  
        M = float(input())
        if 0 <= M < 360: # Program memeriksa apakah input berada dalam rentang antara 0 hingga
            # 359.99 derajat, yang merupakan nilai valid untuk representasi jam di dalam program.
            detik = M * 240 # menghitung jumlah detik yang sesuai dengan nilai sudut input M. dalam konteks ini, 1 derajat setara 240 detik
            jam = ((detik // 3600) + 6) % 24 # Program menghitung jam dengan membagi total detik dengan 3600
            # dan menambahkan 6 jam. Penggunaan modulo 24 digunakan untuk menjamin bahwa jam tetap dalam rentang 0 hingga 23.
            sisa_detik = detik % 3600 # menghitung sisa detik setelah menghitung jam.
            menit = sisa_detik // 60 # Program menghitung menit dengan membagi sisa detik dengan 60 (jumlah detik dalam satu menit).
            detik = sisa_detik % 60 # menghitung sisa detik setelah menghitung menit.

            if jam >= 0 and jam < 6:
                waktu = "Selamat Malam"
            elif jam >= 6 and jam < 12:
                waktu = "Selamat Pagi"
            elif jam >= 12 and jam < 18:
                waktu = "Selamat Siang"
            else:
                waktu = "Selamat Sore"

            print(waktu)
            print(f'{int(jam):02}:{int(menit):02}:{int(detik):02}')
        else:
            print('Invalid input') # Jika input tidak valid (di luar rentang 0-359.99 derajat), program mencetak "Invalid input."   
    except EOFError: # blok penanganan kesalahan untuk menangkap pengecualian EOFError yang akan muncul ketika pengguna mengakhiri program.

        break  # untuk memberhentikan program