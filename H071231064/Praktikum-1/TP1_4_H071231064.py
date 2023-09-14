print("Pengujian Jenis Karakter")
print("-------------------------")

karakter = input("Karakter = ")

uppercase = karakter >= 'A' and karakter <= 'Z'
lowercase = karakter >= 'a' and karakter <= 'z'
digit = karakter >= '0' and karakter <= '9'

print("Huruf Kapital? : {}".format(uppercase))
print("Huruf Kecil? : {}".format(lowercase))
print("Angka? : {}".format(digit))