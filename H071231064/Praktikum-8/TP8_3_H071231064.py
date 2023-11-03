import re

def validasi_username(username):
    pola = r"((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*){5,20}"
    return re.match(pola, username)

def validasi_email(email):
    pola = r"^[a-z]{5,}@[a-z]+\.(com|co\.id)$"
    return re.match(pola, email)

def validasi_password(password):
    pola = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    return re.match(pola, password)


username = input("Masukkan username: ")
email = input("Masukkan email: ")

if validasi_username(username) and validasi_email(email):

    password = input("Masukkan password: ")

    if validasi_password(password):
        
        print("\nRegistrasi berhasil! Halo", username)
    else:
        
        print("\nPassword yang Anda masukkan berisiko dihack. Registrasi gagal.")
else:
    
    print("\nUsername atau email yang Anda masukkan tidak valid dalam sistem. Registrasi gagal!")