# Minta input dari pengguna untuk jumlah urutan Fibonacci yang diinginkan
n = int(input("Masukkan jumlah urutan Fibonacci yang diinginkan: "))

# Nilai awal dari urutan Fibonacci
a, b = 0, 1

# Mencetak urutan Fibonacci pertama n
for i in range(n):
    print(a, end=' ')  # Mencetak nilai a tanpa newline
    c = a
    a = b 
    b = c + b  # Mengupdate nilai a dan b sesuai dengan aturan Fibonacci

print()  # Mencetak newline untuk pemisah
