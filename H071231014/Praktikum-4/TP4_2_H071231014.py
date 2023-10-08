def kata_palindrom(kata):
   kata = kata.lower()
   balik = kata[::-1]
   if kata == balik:
      return "Kata Palindrom"
   else:
      return "Bukan Kata Palindrom"

kata = input("Masukan Kata : ")
hasil = kata_palindrom(kata)
print(f"Kata {kata} Adalah {hasil}")
