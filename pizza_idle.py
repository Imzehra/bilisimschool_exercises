import random 


def kelime_sec():
    kelime_listesi = ["1Can I have Hawaiian pizza? (hawaii pizzası alabilir miyim?)", "2안녕하세요, 마가리타 하나 드실 수 있나요?(merhaba bir margarita alabilir miyim ?)", "3Merhaba bir sucuklu lütfen!"]
    return random.choice(kelime_listesi)

print (kelime_sec())
liste1 = [
  """paket pizza hamuru
     domates sosu
     mozzarella peyniri
     ananas
     jambon
     220.00 TL"""]
liste2 =[
"""  domates
     mozarella
     fesleğen 
     zeytinyağı 
     tuz
     150,00 TL       """    
     ]

liste3 = [
""" mozzarella peyniri
    zeytin
    marine mantar
    sucuk
    kırmızı ve yeşil biber
    360.00 TL
    """]

oyun_resim = [liste1,liste2,liste3]
kullanici_secimi = int(input("hangisini seçiyorsun \n 0-hawaii pizza, \n 1-margarita, \n 2-sucuklu \n "))

print (oyun_resim[kullanici_secimi]) 
    


if kullanici_secimi >= 3 or kullanici_secimi < 0 :
    print ("malesef yanlış bir tuşa bastığınız için kaybettiniz.")

elif kullanici_secimi[0]==liste1 :
    print ("Doğru seçim devam et")

elif kullanici_secimi[1]==liste2 :
    print ("Doğru seçim devam et")

elif kullanici_secimi[3]==liste3 :
    print ("Doğru seçim devam et")

elif kullanici_secimi[0]==liste2 :
    print ("yanlış seçimi yaptınız")

elif kullanici_secimi[0]==liste3 :
    print ("yanlış seçimi yaptınız")

elif kullanici_secimi[1]==liste1 :
    print ("yanlış seçimi yaptınız")

elif kullanici_secimi[1]==liste3 :
    print ("yanlış seçimi yaptınız")

elif kullanici_secimi[2]==liste1 :
    print ("yanlış seçimi yaptınız")

elif kullanici_secimi[2]==liste2 :
    print ("yanlış seçimi yaptınız")





vv
