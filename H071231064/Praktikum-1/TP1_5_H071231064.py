print("Konversi Detik Ke Jam")
print("By A.M.Yusran Mazidan")
print("=======================")

InputDetik = int(input("Masukkan Jumlah Detik : "))
Sisa = InputDetik % 3600
print(f"{InputDetik // 3600 :02d}:{Sisa // 60 :02d}:{Sisa % 60 :02d}")
