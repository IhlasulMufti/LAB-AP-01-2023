print('Pilih Gender Anda')
print('1.Pria')
print('2.Wanita')

gender = int(input('='))

tinggi_awal =float(input('Masukan Tinggi Badan (cm) ='))            
berat = float(input('Masukan Berat Badan (kg) ='))

tinggi = tinggi_awal/100
BMI = (berat/(tinggi**2))

if gender == 1:
    if BMI <18:
        tipe= 'underweight'
    elif 18<= BMI <=22.3:
        tipe= 'normal'
    elif 24<= BMI <=26.9:
        tipe= 'overweight'
    else:
        tipe= 'obese'
elif gender == 2:
    if BMI <17:
        tipe= 'underweight'
    elif  17<= BMI <=23.9:
        tipe= 'normal'
    elif  24<= BMI <=27.9:
        tipe= 'overweight'
    else:
        tipe= 'obese'
else:
    print('data tidak valid')
print(f'anda tergolong {tipe} dengan BMI {BMI:.2f}')