def stringPermutasi(kata):
    try: 
        kata = int(kata)
        print ("Input harus string")
    except ValueError: 
        if len(kata) <= 1:
            return print(kata)
        hasil_permutasi = []
        for i in range(len(kata)):
            kata = kata[-1] + kata[:-1]  
            hasil_permutasi.append(kata)

        print(' | '.join(hasil_permutasi) )

kata =input()
stringPermutasi(kata)

