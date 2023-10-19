def suci_username(email):
    username = email.split("@")[0]
    username = ''.join([namaemail for namaemail in username if namaemail.isalpha()])
    return username

email = input("Masukkan email address: ")
print(suci_username(email))