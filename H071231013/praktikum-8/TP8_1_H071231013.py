import re

def validate_string(input_string):
    pattern = re.compile(r'^[a-zA-Z02468]{40}[13579\s]{5}$')

    if pattern.match(input_string):
        return "True"
    else :
        return "False"

# Meminta input dari pengguna
user_input = input("Masukkan string (harus 45 karakter): ")

result = validate_string(user_input)
print("Output:", result)