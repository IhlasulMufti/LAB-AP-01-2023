print("Konversi Suhu Dari Celcius Ke Kelvin, Reamur, Dan Fahrenheit")
print("By A.M.Yusran Mazidan")

celcius = int(input("Masukkan Suhu Dalam Celcius : "))
print("======================================")

Kelvin = celcius + 273.15
Reamur = celcius * (4/5)
Fahrenheit = (celcius * (9/5)) + 32

print("Hasil Konversi Dari Suhu {} Derajat Celcius ke Kelvin adalah : {} K ".format(celcius,Kelvin))
print("Hasil Konversi Dari Suhu {} Derajat Celcius ke Reamur adalah : {} Re ".format(celcius,Reamur))
print("Hasil Konversi Dari Suhu {} Derajat Celcius ke Fahrenheit adalah : {} F ".format(celcius,Fahrenheit))