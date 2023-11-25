input_string = input("Masukkan kata: ")

panjang_string = len(input_string)

if panjang_string < 3:
    print("Masukkan setidaknya 3 karakter.")
else:
    indeks_tengah = panjang_string // 2

    string_baru = input_string[0] + input_string[indeks_tengah] + input_string[-1]

    print("Hasil:", string_baru)
