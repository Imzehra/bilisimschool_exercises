# GELİŞMİŞ HESAP MAKİNESİ 

def hesap_makinesi () :
    while True :
        print ("Gelişmiş hesap makinesi Operasyonları :")
        print ("1.Toplama")
        print ("2.Çıkarma")
        print ("3.Çarpma")
        print ("4.Bölme")
        print ("5.çıkış")
        
secim = input ("Bir işlem seçiniz( 1/2/3/4/5):")
 
if secim in ("1","2","3","4") :
    sayılar = ("Lütfen Sayıları arasında boşluk bırakarak giriniz örn(3 10 55):")
    sayı_listesi= [float(sayı) for sayı in sayılar.split()]
    
    if  secim == 1 :
        sonuc = sum (sayı_listesi)
    elif secim == 2 :
        sonuc = sayı_listesi [0]
        for sayı in sayı_listesi [1: ]:
            sonuc -= sayı 
    elif secim == 3 :
        sonuc =1 
        for sayi in sayı_listesi :
            sonuc *= sayı 
    elif secim == 4 :
        sonuc = sayı_listesi [0]
        try :
            for sayı in sayı_listesi [1: ]:
                sonuc /= sayi 
            except ZeroDivisionError:  
                print ("Hata!,Bir sayı sıfıra bölünemez")
                continue 

















































