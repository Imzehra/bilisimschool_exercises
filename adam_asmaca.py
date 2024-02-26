# ADAM ASMACA  OYUNU 
import random 
def kelime_sec ():
    kelime_listesi=["minecraft","Harry Potter","zero","Taekwondo"]
    return random.choice (kelime_listesi)
def adam_asmaca_tahtasi (can):
    tahta = [
        """
   +----+
   |    |
        |
        |
        |
        |
        |
================= """ ,

        """
   +----+
   |    |
   O    |
        |
        |
        |
        |
================= """,


        """
   +----+
   |    |
   O    |
   |    |
        |
        |
        |
================= """,

    """
   +----+
   |    |
   O    |
  /|    | 
        |
        |
        |
=================
        """ ,

"""

   +----+
   |    |
   O    |
  /|\   | 
        |
        |
        |
================= """,

"""

   +----+
   |    |
   O    |
  /|\   | 
   \    |
        |
        |
================= """,

"""

   +----+
   |    |
   O    |
  /|\   | 
  /\    |
        |
        |
================= """ 
    ]
    return tahta [6 - can] 

def adam_asmaca_oyunu ():
    secilen_kelime = kelime_sec ()
    kelime_uzunluk = len (secilen_kelime)
    kelime= ['_ ']*kelime_uzunluk 
    can=6
    oyun_sonu=False 
    
    print ("ADAM ASMACA OYUNUNA HOŞ GELDİNİZ")
    while not oyun_sonu :
        tahmin = input ("Bir harf tahmin edniniz: ").lower ()
        if not tahmin.isalpha () or len (tahmin) !=1:
            print ("lütfen geçerli bir harf giriniz")
            continue 
        
        if tahmin in kelime:
            print ("Bu harfi tahmin ettiniz,Tekrar deneyiniz.")
            continue 
        
        if tahmin not in secilen_kelime:
            can-=1
            print ("Yanlış tahmin! Kalan can: {}".format(can))
        
        
        for i in range (kelime_uzunluk):     #bu kod parçası seçilen kelimenin içinde olan herhangi 
                                             #bir harfi kontrol eder ve bulunuyorsa yazar
            harf = secilen_kelime [i]
            if harf==tahmin:
                kelime [i]=harf 
        print (adam_asmaca_tahtasi(can))
        print ("Tahmin durumu: {}".format(' '.join(kelime))) #oyuncunun her tahmin sonu dğr thmn ettiği bş alan
        
        
        
        
        if '_' not in kelime:
            oyun_sonu=True
            print("TEBRİKLER KAZANDINIZ !!!!!!!")
            
            
        elif can == 0 :
            oyun_sonu=True 
            print ("KAYBETTİN DOĞRU KELİME: {}".format (secilen_kelime))
            
adam_asmaca_oyunu ()
        
        
        
        
        

    
        

































































































  





















































