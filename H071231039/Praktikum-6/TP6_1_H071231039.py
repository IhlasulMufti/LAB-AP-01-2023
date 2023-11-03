# ubah jadi fungsi
user_data = {
    "Nama": "",
    "Umur": "",
    "Alamat": ""
}

user_data["Nama"] = input("Input nama: ")
user_data["Umur"] = input("Input umur: ")
user_data["Alamat"] = input("Input alamat: ")

while True:
    print("=" * 50)
    print("Selamat datang", user_data["Nama"])
    print("Silahkan pilih opsi")
    print("=" * 50)
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("=" * 50)
    pilihan = input("Input opsi: ")

    if pilihan == '1':
        print("=" * 50)
        print("Data anda adalah")
        print("Nama:", user_data["Nama"])
        print("Umur:", user_data["Umur"])
        print("Alamat:", user_data["Alamat"])
        print("=" * 50)
    elif pilihan == '2':
        new_nama = input("Silahkan Input nama baru: ")
        user_data["Nama"] = new_nama
        print("Data anda sukses di diperbarui")
    elif pilihan == '3':
        new_umur = input("Silahkan Input umur baru: ")
        user_data["Umur"] = new_umur
        print("Data anda sukses di diperbarui")
    elif pilihan == '4':
        new_alamat = input("Silahkan Input alamat baru: ")
        user_data["Alamat"] = new_alamat
        print("Data anda sukses di diperbarui")
    elif pilihan == '5':
        print("=" * 50)
        print("Selamat Tinggal", user_data["Nama"])
        break
    else:
        print("Opsi tidak valid. Silahkan pilih opsi 1-5.")
