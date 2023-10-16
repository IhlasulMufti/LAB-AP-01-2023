def kata_baru(kata):
      if len(kata) % 2 == 0:
            hasil = kata[0] + kata[len(kata)//2-1]+kata[len(kata)//2] + kata[-1]
            return hasil
      else:
            hasil = kata[0]+kata[len(kata)//2]+kata[-1]  
            return hasil
kata = input("masukkan kata : ")
print(kata_baru(kata))