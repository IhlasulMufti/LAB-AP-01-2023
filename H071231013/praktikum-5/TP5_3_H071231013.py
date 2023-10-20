def is_anagram(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    count1 = {}
    for char in word1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    
    count2 = {}
    for char in word2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
    
    if count1 == count2:
        return True
    else:
        return False

word1 = input("Masukkan kata pertama: ")

word2 = input("Masukkan kata kedua: ")

result = is_anagram(word1, word2)

print(result)