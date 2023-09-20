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
            print("Anda Tergolong Underweight dengan BMI {:.2f}".format(bodyMassIndex)) 
        elif bodyMassIndex >= 18 and bodyMassIndex <= 23.9 :
            print("Anda Tergolong Normal dengan BMI {:.2f}".format(bodyMassIndex)) 
        elif bodyMassIndex >= 24 and bodyMassIndex <= 26.9 :
            print("Anda Tergolong Overweight dengan BMI {:.2f}".format(bodyMassIndex)) 
        else :
            print("Anda Tergolong Obese dengan BMI {:.2f}".format(bodyMassIndex)) 
    case 2:
        if bodyMassIndex < 17 :
            print("Anda Tergolong Underweight dengan BMI {:.2f}".format(bodyMassIndex)) 
        elif bodyMassIndex >= 17 and bodyMassIndex <= 23.9 :
            print("Anda Tergolong Normal dengan BMI {:.2f}".format(bodyMassIndex)) 
        elif bodyMassIndex >= 24 and bodyMassIndex <= 27.9 :
            print("Anda Tergolong Overweight dengan BMI {:.2f}".format(bodyMassIndex)) 
        else :
            print("Anda Tergolong Obese dengan BMI {:.2f}".format(bodyMassIndex)) 
    # case _ :
    #     print("Gender tidak ada")
