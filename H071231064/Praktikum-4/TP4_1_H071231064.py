def stringPermutation(kata):
    try:
        if not isinstance(kata, str):
            raise TypeError("Input harus berupa string")
        
        if len(kata) == 0:
            raise ValueError("Input tidak boleh kosong")
        
        for i in range(0, len(kata)):
            awalKata = kata[:-1]
            akhirKata = kata[-1:]
            kata = akhirKata + awalKata
            print(kata, end=" | ")

    except TypeError as e:
        print(f"Error: {e}")
        kata = input("Masukkan kata baru: ")
        stringPermutation(kata)
    except ValueError as e:
        print(f"Error: {e}")
        kata = input("Masukkan kata baru: ")
        stringPermutation(kata)

try:
    input_kata = input("Masukkan sebuah kata: ")
    stringPermutation(input_kata)
except KeyboardInterrupt:
    print("\nProgram berhenti.")