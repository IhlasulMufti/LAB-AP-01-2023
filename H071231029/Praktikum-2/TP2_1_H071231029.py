print("Pilih gender anda : \n 1.Pria \n 2.Wanita")
gender = int(input("= " ))
tinggi = float(input("Masukkan tinggi anda: " ))
Berat_Badan = float(input("Masukkan Berat badan anda: " ))
bmi = Berat_Badan / ((tinggi/100)**2)

if gender == 1:
    if bmi < 18:
        print(f"Anda tergolong underweight dengan Bmi {bmi:.2f} ")
    elif bmi >= 18 and bmi <= 29.3:
        print(f"Anda tergolong normal dengan Bmi {bmi:.2f} ")
    elif bmi >= 24 and bmi <= 26.9:
        print(f"Anda tergolong overweight dengan bmi {bmi:.2f} ")
    elif bmi >=27:
        print(f"Anda tergolong obese dengan Bmi {bmi:.2f} ")

elif gender == 2:
    if bmi < 17:
        print(f"Anda tergolong underweight dengan bmi {bmi:.2f} ")
    elif bmi >= 17 and bmi <= 29.3:
        print(f"Anda tergolong normal dengan bmi {bmi:.2f} ")
    elif bmi >= 24 and bmi <= 27.9: 
        print(f"Anda tergolong overweight dengan bmi {bmi:.2f} ")
    elif bmi >=28:
        print(f"Anda tergolong obese dengan bmi {bmi:.2f} ")

else:
    print("inputan tidak valid")



 

    