def detail_data():
    print("="*50)
    print("Data anda adalah")
    print(f"Nama:{data['nama']}")
    print(f"Umur:{data['umur']}")
    print(f"Alamat:{data['alamat']}")
    
def ganti_nama(data):
    nama_baru= input("Silahkan input nama baru: ")
    data["nama"] = nama_baru
    print("Data anda sukses diperbarui")
    return data

def ganti_umur(data):
    umur_baru= int(input("Sialhkan input umur baru: "))
    data["umur"]= umur_baru
    print("Data anda sukses diperbarui")
    return data

def ganti_alamat(data):
    alamat_baru= input("Sialhkan input alamat baru: ")
    data["alamat"]= alamat_baru
    print("Data anda sukses diperbarui")
    return data
    
print("Untuk memulai silahkan input data anda")
data={
    "nama":"",
    "umur":"",
    "alamat":""
}
data["nama"]= input("Input Nama: ")
data["umur"]= int(input("Input Umur: "))
data["alamat"]= input("Input Alamat: ")

data2={
    "nama":"",
    "umur":"",
    "alamat":""
}
data2["nama"]= input("Input Nama: ")
data2["umur"]= int(input("Input Umur: "))
data2["alamat"]= input("Input Alamat: ")

data3={
    "nama":"",
    "umur":"",
    "alamat":""
}
data3["nama"]= input("Input Nama: ")
data3["umur"]= int(input("Input Umur: "))
data3["alamat"]= input("Input Alamat: ")


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
            new_name = input
            data, = ganti_nama(data, new_name)
        case 3:
            ganti_umur()
        case 4:
            ganti_alamat()
        case 5:
            print(f"Selamat tinggal {data['nama']}")
            break
        case _:
            print("Opsi Tidak Tersedia")
