angka = list(map(int, input("Masukkan beberapa angka: ").split()))

couple = {}

for i in angka:
    if i in couple:
        couple[i] += 1
    else:
        couple[i] = 1

jumlah_pasangan = sum(value // 2 for value in couple.values())
print(f"{jumlah_pasangan} pasangan")