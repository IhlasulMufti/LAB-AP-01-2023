tinggi_cm = float(input("Masukkan tinggi badan (cm): "))
berat_kg = float(input("Masukkan berat badan (kg): "))
jenis_kelamin = input("Masukkan jenis kelamin (pria/wanita): ")

tinggi_m = tinggi_cm / 100
bmi = berat_kg / (tinggi_m ** 2)

if jenis_kelamin.lower() == 'pria':
    if bmi < 18.5:
        tipe = "underweight"    
    elif 18.5 <= bmi <= 24.9:
        tipe = "normal"
    elif 25 <= bmi < 29.9:
        tipe = "overweight"
    else:
        tipe = "obese"
    print(f"BMI Anda adalah {bmi:.2f}, Anda termasuk dalam kategori {tipe}")        
elif jenis_kelamin.lower() == 'wanita':
    if bmi < 18.5:
        tipe ="underweight"       
    elif 18.5 <= bmi < 24.9:
        tipe = "normal"      
    elif 25 <= bmi < 29.9:
        tipe = "overweight"  
    else:
        tipe = "obese"

    print(f"BMI Anda adalah {bmi:.2f}, Anda termasuk dalam kategori {tipe}")
else:
    print("Input jenis kelamin tidak valid. Harap masukkan 'pria' atau 'wanita'.")