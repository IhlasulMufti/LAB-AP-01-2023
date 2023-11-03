while True:
    try:
        derajat = float(input(""))
        if derajat >= 360 or derajat < 0:
            print('Inputan harus diantara 0-360')
        else:
            total_detik = int(derajat * 240) + (6*3600)
            if total_detik >= (24*3600):
                total_detik = total_detik-(24*3600)
            jam = total_detik//3600
            menit = (total_detik % 3600)//60
            sisadetik = total_detik % 60
            if 6 <= jam < 11:
                print("Selamat pagi")
            elif 11 <= jam < 15:
                print("Selamat siang")
            elif 15 <= jam < 18:
                print("Selamat sore")
            else:
                print("Selamat malam")

            print(f"{jam:02}:{menit:02}:{sisadetik:02}")
    except:
        print("End of file")
        break
