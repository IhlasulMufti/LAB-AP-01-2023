def mutasi(kata):
    try:
        angka = int(kata)
        print ("inputan harus berupa string")
    except:
        for i in range(len(kata)):
            kata = kata[-1] + kata[:-1]
            print (kata, end=" | ")
kata = input("Masukan kata : ")
mutasi(kata)