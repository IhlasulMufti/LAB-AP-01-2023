print("Menghitung Body Mass Index")
print("By A.M.Yusran Mazidan")
print("=============================")

gender = int(input("Masukkan Gender Anda : \n1. Pria \n2. Wanita \n= "))
if gender >2 :
    print("gender tersebut tidak ada")


tinggi = float(input("Masukkan Tinggi Badan : "))
berat = float(input("Masukkan Berat Badan : "))

bodyMassIndex = berat/(tinggi/100)**2

match gender :
    case 1:
        if bodyMassIndex < 18 :
            golongan = "Underweight"
        elif bodyMassIndex >= 18 and bodyMassIndex <= 23.9 :
            golongan = "Normal"
        elif bodyMassIndex >= 24 and bodyMassIndex <= 26.9 : 
            golongan = "Overweight"
        else :
            golongan = "Obese"
    case 2:
        if bodyMassIndex < 17 :
            golongan = "Underweight"
        elif bodyMassIndex >= 17 and bodyMassIndex <= 23.9 :
            golongan = "Normal" 
        elif bodyMassIndex >= 24 and bodyMassIndex <= 27.9 :
            golongan = "Overweight" 
        else :
            golongan = "Obese" 
    # case _ :
    #     print("Gender tidak ada")

print("Anda Tergolong {} Dengan BMI {:.2f}".format(golongan,bodyMassIndex))
