# def jam(masukan_derajat):
selamat = [["Pagi",32400],["Siang",54000],["Sore",64800],["Malam",86400]]
while True:
    # masukan_derajat = str(input('jhkk : '))

    try:
        masukan_derajat = float(input("masukkan derajat : "))
    except EOFError:
        print("Nilai bukan float")
        break
    else:
            if masukan_derajat >= 0:
                persen_derajat = masukan_derajat / 360
                # print(persen_derajat)
                # 86400 detik sama dengan 24 jam
                waktu = 86400 * persen_derajat
                if waktu < 64800:
                    offset_waktu = waktu + 21600
                else:
                    offset_waktu = waktu - 64800
                # print(waktu)
                sisa =  offset_waktu % 3600

                for waktu_matahari in selamat:
                    if offset_waktu - waktu_matahari[1] < 0:
                        # print(offset_waktu - waktu_matahari[1])
                        print("Selamat {}".format(waktu_matahari[0]))
                        break

                print("{:02}:{:02}:{:02}".format(int(offset_waktu // 3600),int(sisa // 60),int(sisa % 60)))

        # for i in range(360+1):
        #     jam(i)


