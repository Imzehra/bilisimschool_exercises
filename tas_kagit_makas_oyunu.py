
import random 
tas = '''
    _________
---'    _____) 
      (_______)
      (_______)   
      (______)
-----(______)
'''      
        
kagit = '''
        
      ________
-----'________)___
      ____________)__  
      _______________)
      _____________)  
      __________)
-----'  
      
'''    
makas = '''
      
    ________
---'________)___     
    ____________)__
    _______________)    
    (______)  
----(_____)    
      '''
      
oyun_resim = [tas,kagit,makas]
kullanici_secimi = int(input("hangisini seçiyorsun \n 0-tas, \n 1-kağıt \n 2-makas \n "))
      
print (oyun_resim[kullanici_secimi]) 
    
pc_secim = random.randint (0,2) 
      
print ("Bilgisayar'ın seçimi: ")
print ( oyun_resim [pc_secim] ) 
    
if kullanici_secimi >= 3 or kullanici_secimi < 0 :
    print ("malesef yanlış bir tuşa bastığınız için kaybettiniz.")
elif kullanici_secimi > pc_secim:
    print ("Kazandınız!!!")
elif pc_secim > kullanici_secimi :
    print ("Kaybettiniz!!!")   
elif kullanici_secimi == 0 and pc_secim == 0 :
    print ("Kazandınız!!!")
elif pc_secim == 0 and kullanici_secimi  == 0 :
    print ("Kaybettiniz!!!")  
elif pc_secim == kullanici_secimi :
    print ("Berabere!")


