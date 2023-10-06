print("Masukkan angka yang diinginkan\nKetik Selesai Jika Ingin Berhenti")
angka = []
try:

    while True:
        x = int(input())
        angka.append(x)
except ValueError:
    print(angka)

def terbesar(angka):
    terbesar = angka[0]
    for i in angka:
        if i > terbesar:
            terbesar = i
    return terbesar

print(f"nilai terbesarnya adalah : {terbesar(angka)}")

