def is_palindrome(word: str) -> str:

    cleaned_word = "".join(word.split()).lower()

    if cleaned_word == cleaned_word[::-1]:

        return "Palindrom"
    else:
        return "Bukan Palindrom"

input_word = input("Masukkan kata palindrom: ")
hasil = is_palindrome(input_word)

print(hasil)
hasil = (f'Bukan Palindrom')

input_word = input("Masukkan kata: ")
hasil = is_palindrome(input_word)

print(hasil)
hasil = (f'Bukan Palindrom')