# Menerima input detik
detik = int(input("Masukkan jumlah detik: "))

# Menghitung jam, menit, dan sisa detik
jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik_sisa = sisa_detik % 60

# Membuat format waktu dengan dua digit
jam_str = str(jam).zfill(2)
menit_str = str(menit).zfill(2)
detik_str = str(detik_sisa).zfill(2)

# Menampilkan hasil
print(f"Format waktu: {jam_str}:{menit_str}:{detik_str}")
