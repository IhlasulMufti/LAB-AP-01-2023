while True:
    try:
        derajat = float(input())
        if 0 <= derajat < 360:
            total_detik = int(derajat * 240 + 21600) % 86400
            jam = total_detik // 3600
            sisa = total_detik % 3600
            menit = sisa // 60
            detik = sisa % 60

            if 6 <= jam < 11:
                waktu = "Pagi"
            elif 11 <= jam < 15:
                waktu = "Siang"
            elif 15 <= jam < 18:
                waktu = "Sore"
            else:
                waktu = "Malam"

            print(f"Selamat {waktu}\n{jam:02}:{menit:02}:{detik:02}")
        else :
            print ('tidak memenuhi')
    except ValueError:
        print("end of file")
        break


