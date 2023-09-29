detik = int(input("masukkan detik = "))

jam = detik// 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print("{:02}:{:02}:{:02}".format(jam, menit, detik))