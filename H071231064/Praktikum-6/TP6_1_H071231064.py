biodatauser = {
    "nama": "",
    "umur": "",
    "alamat": "",
}

def input_biodata():
    biodatauser["nama"] = input("Input nama: ")
    biodatauser["umur"] = input("Input umur: ")
    biodatauser["alamat"] = input("Input alamat: ")

def detail_biodata():
    print("=" * 55)
    print("Data Anda adalah:")
    for key, nilai in biodatauser.items():
        print(f"{key}: {nilai}")

def ubah_data(item):
    biodatauser[item] = input(f"Silakan Input {item} baru: ")
    print("Data anda sukses diperbarui")

def simplecrud():
    if biodatauser["nama"] == "" or biodatauser["umur"] == "" or biodatauser["alamat"] == "":
        print("Selamat datang! Untuk memulai, silahkan input data anda")
        input_biodata()

    print("=" * 12)
    print("Selamat datang {}! Silahkan pilih opsi".format(biodatauser["nama"]))
    print("=" * 12)
    print("1. Detail anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar\n")
    print("=" * 12)

    opsi_inputan = int(input("Input opsi:"))
    print("=" * 12)

    match opsi_inputan:
        case 1:
            detail_biodata()
        case 2:
            ubah_data("nama")
            print("Data anda sukses diperbarui")
        case 3:
            ubah_data("umur")
            print("Data anda sukses diperbarui")
        case 4:
            ubah_data("alamat")
            print("Data anda sukses diperbarui")
        case 5:
            quit()
        case _:
            print("Pilihan tidak valid.")
    
    simplecrud()

simplecrud()
