def anagram(s1,s2):
    for i in s1:
        if s1.count(i) != s2.count(i):
            return False
    return True
s1 = input().replace(' ', '').lower()
s2 = input().replace(' ', '').lower()
print(anagram(s1,s2))