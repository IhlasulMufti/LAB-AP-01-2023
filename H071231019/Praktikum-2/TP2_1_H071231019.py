gender = int(input("Pilih gender Anda:\n1. Pria\n2. Wanita\n= "))

if gender != 1 and gender != 2: #tidak dieksekusi jika g-nya 1 atau 2
    print("Pilih input yang valid")
else: #dieksekusi jika gendernya 1 atau 2
    tinggi = float(input("Masukkan tinggi badan (cm) : ")) / 100
    berat = float(input("Masukkan berat badan (kg) : ")) 
    BMI = float(input("Input BMI: "))

    # BMI = berat / tinggi**2

    if gender == 1: # jika pria ini yang dieksekusi
        if 27 <= BMI:
            kategori = "Obese"
        elif 24 <= BMI < 27:
            kategori = "Overweight"
        elif 18 <= BMI < 24:
            kategori = "Normal"
        else:
            kategori = "Underweight"
    else: # jika wanita ini yang dieksekusi
        if 28 <= BMI:
            kategori = "Obese"
        elif 24 <= BMI < 28:
            kategori = "Overweight"
        elif 17 <= BMI < 24:
            kategori = "Normal"
        else:
            kategori = "Underweight"

    print(f"Anda tergolong {kategori} dengan BMI {BMI:.2f}")
    