print("Masukkan angka : ")
angka = []
try:
    while True:
        x = int(input())
        angka.append(x)
except ValueError as msg:
    print('Terjadi kesalahan karena {msg}')

def terbesar(angka):
    terbesar = angka[0]
    for i in angka:
        if i > terbesar:
            terbesar = i
    return terbesar


print(angka)
print(f"nilai terbesarnya adalah : {terbesar(angka)}")
