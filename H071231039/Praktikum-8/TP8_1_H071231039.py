import re
def validasi_string(string):
    pola = r'^[a-zA-Z2468]{40}[13579\s]{5}$'
    cocok = re.search(pola, string)

    if len(string) == 45:
        if cocok:
            return True
        else:
            return False
    else:
        return False
    
    
User = input()
result = validasi_string(User)
print(result)