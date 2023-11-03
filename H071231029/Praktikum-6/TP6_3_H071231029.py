x = input("Masukkan Beberapa angka: ").split()
x=[int(i)for i in x]
genap= [i for i in  x if i%2== 0]
ganjil=[i for i in x if  i%2 != 0]
habis_dbagi_5 =[ i for i in x if i%5 ==0]

print(f"ini adalah bilangan genap{genap} ,\nini adalah bilangan ganjil{ganjil},\nini adalah bilangan ganjil{habis_dbagi_5}")



