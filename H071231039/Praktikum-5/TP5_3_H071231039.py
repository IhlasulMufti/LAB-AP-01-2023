def anagram(kata1, kata2):
    beda = 0
    kata1 = kata1.replace(' ', '').lower()
    kata2 = kata2.replace(' ', '').lower()

    for huruf in kata1:
        cek1 = kata1.count(huruf)
        cek2 = kata2.count(huruf)
        if cek1 != cek2:
            beda += 1

    if beda == 0 and len(kata1) == len(kata2):
        return True
    else:
        return False


print('='*50, '\nSelamat Datang di Program Pengujian Anagram')
print('='*50)
kata1 = input('\nMasukkan kata pertama: ')
kata2 = input('Masukkan kata pertama: ')
print(f'\nHasilnya adalah: {anagram(kata1, kata2)}')
