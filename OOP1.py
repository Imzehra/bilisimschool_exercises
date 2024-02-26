#OBJECT ORIENTED PROGRAMMING ( OOP )
#NESNE TABANLI PROGRAMLAMA

class Car():     #sınıfların baş harfleri büyük yazılır.
    kapi_sayisi=2
    motor_gucu=500
    renk="mavi"

arabam=Car() #araba nesnesi oluşturduk ve car sınıfını buna atadık.
print(arabam.renk)
print(arabam.kapi_sayisi)


#OOP her işlevin nesnel olarak soyutlandığı bir programlama şeklidir.
#yani gerçek hayattaki birçok nesnenin bilgisayar ortamına aktarılmasıdır.
#Class nedir? -değişkenleri ve fonksiyonları bir arada saklayabilen sistemdir.
#Nesne nedir? -içinde veri saklayan ve bu veriler üzerinde işlem yapacak olan metotları
#-bulunduran yapılardır.

x="mert"
print(type(x))

# neye sahiptir? ---> (özellik) attribute

# ne yapar? ---> method

#TELEFON ÖRNEĞİ
#kaç mp kamera ---> özellik
#kaç gb ram    ---> özellik
#dokunmatik mi tuşlu mu ---> özellik
#ekranı kaç inç? ---> özellik

#arama yapmak ---> metot
#mesaj gönderir --->metot
#fotoğraf çeker --->metot

#NOT: class yapılarında PascalCase yazım şekli kullanılır.

class Calisan () : 
    unvani = "işçi"
    maasi = 20000
    memleketi = " "
    dogum_tarihi = " "
    
    
yagiz=Calisan ()
ahmetemir=Calisan ()

print (yagiz.maasi)
print (ahmetemir.unvani)
