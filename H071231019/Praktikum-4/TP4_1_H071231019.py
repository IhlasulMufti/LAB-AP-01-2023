def permutasi_kata(kata):
    try:
        int(kata)
        print('Inputan harus berupa string')
    except:
        for i in range(len(kata)):
            kata = kata[-1] + kata[:-1]
            print(kata,end=" | ")

permutasi_kata(input("Masukkan kata: "))