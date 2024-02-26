import random 

hedef_sayi=random.randint(1,2)
deneme = 0

while True :
    tahmin = int(input("bir sayı tahmin ediniz: "))
    deneme+=1
    
    if tahmin<hedef_sayi:
        print("daha yüksek bir sayı tahmin ediniz")
    elif tahmin>hedef_sayi:
        print("daha düşük bir sayı tahmin ediniz")
    else: 
        print (f"Tebrikler,{hedef_sayi}'ı {deneme} denemede buldunuz")
        break 

































