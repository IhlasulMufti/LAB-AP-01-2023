# #nomor 2 (konversi suhu)
print('Konversi Suhu dari Celcius ke Kelvin, Reamur, dan Fahreinheit')
c= int(input('Masukkan Suhu Dalam Celcius: '))

K= int(c+273)
R= int((4/5)*c) 
F= int((9/5*c)+32)


print('Hasil Konversi dari {} Derajat ke Kelvin Adalah: {}K'.format(c,K))
print(f'Hasil Konversi dari {c} Derajat ke Reamur Adalah: {R}R')
print(f'Hasil Konversi dari {c} Derajat ke Fahreinheit Adalah: {F}F')