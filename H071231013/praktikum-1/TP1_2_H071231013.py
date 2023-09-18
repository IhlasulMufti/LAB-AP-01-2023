# Input suhu dalam Celcius
suhu_celcius = float(input("Masukkan suhu dalam Celcius: "))

# Konversi ke Kelvin
suhu_kelvin = int(suhu_celcius + 273)

# Konversi ke Reamur
suhu_reamur = int((4 / 5) * suhu_celcius)

# Konversi ke Fahrenheit
suhu_fahrenheit = int((suhu_celcius * 9 / 5) + 32)

# Menampilkan hasil konversi
print(f"Suhu dalam Kelvin: {suhu_kelvin}")
print(f"Suhu dalam Reamur: {suhu_reamur}")
print(f"Suhu dalam Fahrenheit: {suhu_fahrenheit}")
