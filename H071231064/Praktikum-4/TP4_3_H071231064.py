daftar = []
def maksimum(daftar_angka):
    nilai_banding = 0
    for i in range(0,len(daftar_angka)):
        # print(nilai_banding)
        if(int(daftar_angka[i]) > int(nilai_banding)):
            nilai_banding = daftar_angka[i]
    print(">> ",nilai_banding)

masukan_bool = "t"
while True:
    angka = input("masukkan angka : ")
    # masukan_bool = input("apakah selesai memasukkan angka baru? : ")
    if(angka == "selesai"):
        maksimum(daftar)
        break
    daftar.append(angka)