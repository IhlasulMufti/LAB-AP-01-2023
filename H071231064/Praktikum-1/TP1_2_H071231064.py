print("Konversi Suhu Dari Celcius Ke Kelvin, Reamur, Dan Fahrenheit")
print("By A.M.Yusran Mazidan")

celcius = int(input("Masukkan Suhu Dalam Celcius : "))
print("======================================")

Kelvin = celcius + 273.15
Reamur = celcius * (4/5)
Fahrenheit = (celcius * (9/5)) + 32

print(f"Hasil Konversi Dari Suhu {celcius} Derajat Celcius ke Kelvin adalah : {int(Kelvin)} K ")
print(f"Hasil Konversi Dari Suhu {celcius} Derajat Celcius ke Kelvin adalah : {int(Reamur)} Re ")
print(f"Hasil Konversi Dari Suhu {celcius} Derajat Celcius ke Kelvin adalah : {int(Fahrenheit)} F ")