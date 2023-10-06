while True:
    try:
        M = float(input())
        if 0 <= M < 360:
            s = M * 240 
            jam = ((s // 3600) + 6) % 24
            sisa_s = s % 3600
            menit = sisa_s // 60
            detik = sisa_s % 60

            if 6 <= jam < 12:
                print('Selamat Pagi')
            elif 12 <= jam < 18:
                print('Selamat Siang')
            elif 18 <= jam < 24:
                print('Selamat Sore')
            else:
                print('Selamat Malam')

            print(f'{int(jam):02}:{int(menit):02}:{int(detik):02}')
        else:
            print('Invalid Input')
    except EOFError:

        break                               
