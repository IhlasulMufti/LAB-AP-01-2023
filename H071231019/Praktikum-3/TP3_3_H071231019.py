while True:
    try:
        derajat = float(input("Masukkan nilai derajat : "))
       
        total_detik = derajat * 240 + (6 * 3600) 
        total_detik = int(total_detik)  
        
        if total_detik >= (24 * 3600):
            total_detik = total_detik - (24 * 3600)  
        jam = total_detik // 3600 
        menit = (total_detik % 3600) // 60 
        sisadetik = total_detik % 60

        if 6 <= jam < 12:
            print("Selamat Pagi")
        elif 12 <= jam < 15:
            print("Selamat Siang")
        elif 15 <= jam < 18:
            print("Selamat Sore")
        else:
            print("Selamat Malam")

        print(f"{jam:02}:{menit:02}:{sisadetik:02}")
    except ValueError:
        print("End Of File")
        break
