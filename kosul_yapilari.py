#KOÅUL YAPILARI
sayi = int (input ("bir sayÄ±nÄ±z giriniz: "))
if sayi%2==0:
    print (sayi, "nu sayÄ± Ã§ift bir sayÄ±dÄ±r.")
else:
    print (sayi,"bu sayÄ± tek sayÄ±dÄ±r")
#sayÄ± deÄiÅkeni iÃ§erisine kullanÄ±cÄ±dan alÄ±nan sayÄ±yÄ± atadÄ±k ve fonksiyonu ile bu
#sayÄ±yÄ± tam sayÄ±ya Ã§evirdik.Daha sonra sÄ±rasÄ±yla
#sayÄ±yÄ± 2ye bÃ¶ldÃ¼ÄÃ¼mÃ¼zde kalan sayÄ± 0 eÅitmi diye kontrol ettik
#eÄer il koÅul (if) saÄlanmazsa ardÄ±ndan diÄer koÅul (else) devreye girdi.

#ÃOKLU KOÅULLAR
sinav1 = int (input ("1.sÄ±nav notunuzu giriniz: "))
sinav2 = int (input ("2.sÄ±nav notunuzu giriniz: "))
ortalama = (sinav1+sinav2) / 2
if  ortalama>=85:
    print ("PEKÄ°YÄ°")
elif ortalama>=70:
    print ("Ä°YÄ°")
elif ortalama>=60:
    print ("ORTA")
elif ortalama>=45:
    print("GEÃER")
else:
    print ("KALDIN")
"""

"""
#Ä°Ã Ä°ÃE KOÅULLAR
ÄSÄM = input ("isminizi giriniz: ")
soyisim = input ("soyisminizi giriniz: ")
e_mail = input ("e-mailinizi giriniz: ")
kullanci_adi = input ("kullanÄ±cÄ± adÄ±nÄ±zÄ± giriniz: ")
sifre = input ("Åifrenizi giriniz: ")
print (f"Merhaba {ÄSÄM} {soyisim} hesabÄ±nÄ±z baÅarÄ±yla oluÅturuldu! ")
print ("Devam etmek iÃ§in lÃ¼tfen giriÅ yapÄ±nÄ±z! ") 

kullanci_adi2 = input ("KullanÄ±cÄ± adÄ±nÄ±zÄ± giriniz: ")
sifre2 = input ("Åifrenizi giriniz")
if kullanci_adi == kullanci_adi2:
    if sifre == sifre2:
        print ("Sisteme baÅarÄ±yla giriÅ yapÄ±ldÄ±!")
    else:
        print ("Åifreler eÅleÅmedi sisteme girilemedi")
else:
    print ("KullanÄ±cÄ± adÄ± hatalÄ± sisteme girilemedi")

