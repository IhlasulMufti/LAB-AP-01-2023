print("Selamat datang, untuk memulai silakan input data Anda!")
print("="*60)
nama = input("Input nama: ")
umur = input("Input umur: ")
alamat = input("Input alamat: ")

data = {
"nama": nama,
"umur": umur,
"alamat": alamat
}

while True:
    print("="*60)
    print("Selamat datang", data["nama"]+ ", silakan pilih opsi: ")
    print("="*60)
    print("1. Detail Anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("="*60)

    opsi = input("Input opsi: ")

    if opsi == "1":
        print("="*60)
        print("Data Anda adalah")
        print("Nama:", data["nama"])
        print("Umur:", data["umur"])
        print("Alamat:", data["alamat"])
        print()
    elif opsi == "2":
        nama_baru = input("Silakan Input nama baru: ")
        data["nama"] = nama_baru
        print("Data Anda sukses diperbarui")
    elif opsi == "3":
        umur_baru = input("Silakan Input umur baru: ")
        data["umur"] = umur_baru
        print("Data Anda sukses diperbarui")
    elif opsi == "4":
        alamat_baru = input("Silakan Input alamat baru: ")
        data["alamat"] = alamat_baru
        print("Data Anda sukses diperbarui")
    elif opsi == "5":
        print("="*60)
        print("Selamat tinggal", data["nama"])
        break
    else:
        print("Opsi tidak valid, silakan coba lagi!")