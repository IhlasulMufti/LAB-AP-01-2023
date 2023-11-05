import re

def validasi_username(username):
    return re.fullmatch("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{5,20}$", username) is not None

def validasi_email(email):
    return re.match("^[a-z]+[0-9]*@[a-z]+\.[a-z]+(\.[a-z]+)?[0-9]{0,2}$", email) is not None

def validasi_password(password):
    return re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password) is not None

username = input("Masukkan username: ")
email = input("Masukkan email: ")
password = input("Masukkan password: ")

if validasi_username(username):
    print("Username memenuhi syarat.")
else:
    print("Username tidak memenuhi syarat.")

if validasi_email(email):
    print("Email memenuhi syarat.")
else:
    print("Email tidak memenuhi syarat.")

if validasi_password(password):
    print("Password memenuhi syarat.")
else:
    print("Password tidak memenuhi syarat.")
