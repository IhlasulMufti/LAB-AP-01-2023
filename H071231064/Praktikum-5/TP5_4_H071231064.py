def kebalikan(kalimat):
    # kata_jelek = kalimat.find("jelek")
    hasil = kalimat
    kalimat = kalimat.split()
    i = 0
    index_tidak = 0
    index_jelek = 0
    awal_kata = ""
    akhir_kata = ""

    for kata in kalimat:
        if kata.lower() == "tidak":
            index_tidak = i
        elif kata.lower() == "jelek":
            index_jelek = i
        i += 1
    awal_kata = kalimat[:index_tidak]
    akhir_kata = kalimat[index_jelek + 1:]

    if index_tidak > 0:
        if index_tidak < index_jelek:
            hasil = ""
            for kata_awal in awal_kata:
                hasil += kata_awal
                hasil += " "
            hasil += "bagus "
            for kata_akhir in akhir_kata:
                hasil += kata_akhir
                hasil += " "
            return hasil
        else:
            return hasil
    else:
        return hasil
    
kalimattest = input("Input Kalimat :")
print(kebalikan(kalimattest))
