print("Pengujian Jenis Karakter")
print("-------------------------")

karakter = input("Karakter = ")

print(f"Huruf Kapital? : {karakter.isupper()}")
print(f"Huruf Kecil? : {karakter.islower()}")
print(f"Angka? : {karakter.isdigit()}")