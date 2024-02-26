import random 

def sayi_tahmin ():
    while True :
        rastgele_sayi=random.randint (1,100)
        i=0
        while i<5:
            tahmin=int(input("bir sayı giriniz: "))
            i=i+1
            if tahmin==rastgele_sayi:
                    print ("KAZANDIN!!")
                    break 
            elif tahmin<rastgele_sayi:
                print ("hayır daha yüksek bir sayı söyle")
            elif tahmin>rastgele_sayi:
                print ("hayır daha düşük bir sayı söle")
        else:
            print ("KAYBETTİN !!!!!!",rastgele_sayi)
sayi_tahmin ()
