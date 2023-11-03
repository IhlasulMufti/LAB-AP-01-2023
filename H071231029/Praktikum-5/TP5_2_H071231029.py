def membuat_string_baru(mencoba_str):
    if len(mencoba_str) < 3:
        return  "stringg harus lebih dari 3 karakterr"
    
    huruf1 = mencoba_str[0]
    index_tengah = len(mencoba_str) // 2
    huruf_tengah = mencoba_str[index_tengah]
    huruf3 = mencoba_str[-1]
    index_tengah_Genap = index_tengah - 1
    huruf_tengah_genap = mencoba_str[index_tengah_Genap]

    if len(mencoba_str) % 2 == 0:
        string_baru = huruf1 + huruf_tengah_genap+ huruf_tengah + huruf3
    else:
        string_baru = huruf1 + huruf_tengah + huruf3

    return string_baru

mencoba_str = input("Masukkan String: ")
result = membuat_string_baru(mencoba_str)
print(result)
