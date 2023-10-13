def kucing_tikus(KucingA, KucingB,Tikus):

        jarak_A = (KucingA-Tikus)
        if jarak_A<0:
                jarak_A=-(KucingA-Tikus)

        jarak_B = (KucingB-Tikus)
        if jarak_B<0:
                jarak_B=-(KucingB-Tikus)

        if jarak_A > jarak_B:
                print("Cat B")                                   
        elif jarak_B > jarak_A:
                 print("Cat A")
        else:
                 print("Mouse C")
               
kucingA= int(input(">>Cat A= "))
kucingB= int(input(">>Cat B= "))
Tikus = int(input(">>Mos C= "))
print("=" *10)
kucing_tikus(kucingA, kucingB, Tikus)
print("=" * 10)