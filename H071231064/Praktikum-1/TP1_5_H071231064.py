print("Konversi Detik Ke Jam")
print("By A.M.Yusran Mazidan")
print("=======================")

inputDetik = int(input("Masukkan Jumlah Detik : "))
sisa = inputDetik % 3600
# print(f"{InputDetik // 3600 :02}:{Sisa // 60 :02}:{Sisa % 60 :02}")
print("{:02}:{:02}:{:02}".format(inputDetik // 3600,sisa // 60,sisa % 60))
