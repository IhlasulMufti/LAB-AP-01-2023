print('Pilih Gender Anda \n1. Pria \n2. Wanita')

gender = float(input('= '))
if gender!=1 and gender!=2:
    print('Harap memilih pilihan 1 atau 2')
    exit()
else:
    tinggi = float(input('Masukkan tinggi badan (cm) : '))
    berat = float(input('Masukkan berat badan (kg) : '))

bmi = berat/((tinggi/100)**2)

if gender==1: 
    if bmi<18:
        tipe = 'Underweight'
    elif bmi>=18 and bmi<24:
        tipe = 'Normal'
    elif bmi>=24 and bmi<27:
        tipe = 'Overweight'
    else:
        tipe = 'Obese'

elif gender==2:
    if bmi<17:
        tipe = 'Underweight'
    elif bmi>=17 and bmi<24:
        tipe = 'Normal'
    elif 24<= bmi <28:
        tipe = 'Overweight'
    else:
        tipe = 'Obese'

print('Anda tergolong {} dengan BMI {:.2f}'.format(tipe,bmi))
