def detail_data():
    print("="*50)
    print("Data anda adalah")
    print(f"Nama:{data['nama']}")
    print(f"Umur:{data['umur']}")
    print(f"Alamat:{data['alamat']}")
    
def ganti_nama():
    nama_baru= input("Silahkan input nama baru: ")
    data["nama"]= nama_baru
    print("Data anda sukses diperbarui")

def ganti_umur():
    umur_baru= int(input("Sialhkan input umur baru: "))
    data["umur"]= umur_baru
    print("Data anda sukses diperbarui")

def ganti_alamat():
    alamat_baru= input("Sialhkan input alamat baru: ")
    data["alamat"]= alamat_baru
    print("Data anda sukses diperbarui")
    
print("Untuk memulai silahkan input data anda")
data={
    "nama":"",
    "umur":"",
    "alamat":""
}
data["nama"]= input("Input Nama: ")
data["umur"]= int(input("Input Umur: "))
data["alamat"]= input("Input Alamat: ")


while True:
    print("="*50)
    print(f"Selamat datang {data['nama']} silahkan pilih opsi")
    print("="*50)
    print("1.Detail Anda")
    print("2.Ganti Nama")
    print("3.Ganti Umur")
    print("4.Ganti Alamat")
    print("5.Keluar")
    print("="*50)
    opsi = int(input("Input Opsi: "))

    match opsi:
        case 1:
            detail_data()
        case 2:
            ganti_nama()
        case 3:
            ganti_umur()
        case 4:
            ganti_alamat()
        case 5:
            print(f"Selamat tinggal {data['nama']}")
            break
        case _:
            print("Opsi Tidak Tersedia")
