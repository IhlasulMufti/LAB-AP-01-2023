c = float(input("Masukkan suhu dalam Celsius: "))

# Mencari Kelvin
k = c + 273 
print(f"Suhu dalam Kelvin adalah: {int(k)}K") 

# Mencari Reamur
r = 4/5 * c
print(f"Suhu dalam Reamur adalah: {int(r)}°R")

# Mecari Fahrenheit
f = 9/5 * c + 32
print("Suhu {} dalam Fahrenheit adalah: {}°F".format(int(c),int(f)))