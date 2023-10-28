print("Selamat datang untuk memulai silahkan input data anda:")
data = {
    "nama":input("Masukkan Nama anda: "),
    "umur":int(input("Masukkan umur anda: ")),
    "alamat":input("Masukkan Alamat anda: ")
}

while True:
    print("="*50)
    print(f"Selamat datang {data['nama']} silahkan Pilih Opsi anda: ")
    print("="*50)
    print("1.Detail anda\n2.ubah Nama\n3.ubah Umur\n4.ubah Alamat\n5.Keluar")
    menu = int(input("= "))
    print("="*50)
    if menu == 5:
        print (f"Selamat tinggal {data['nama']}")
        break
    elif menu == 1 or menu == 2 or menu == 3 or menu == 4:
        if menu == 1:
            print(f"Data anda adalah:\nNama :{data['nama']}\nUmur:{data['umur']}\nAlamat:{data['alamat']}")
        elif menu == 2:
            data["nama"]=input("Silahkan input nama baru: ")
            print("selama data anda telah diperbaharui")
        elif menu ==3:
            data["umur"]=input("Silahkan input umur baru: ")
            print("selama data anda telah diperbaharui")
        elif menu == 4:
            data["alamat"]=input("Silahkan input alamat baru: ")
            print("selama data anda telah diperbaharui")