#Yapıcı METHODLAR __init__ 

class Person :
    def __init__ (self,isim,yas,cinsiyet,memleket):
        self.isim=isim
        self.yas=yas
        self.cinsiyet=cinsiyet 
        self.memleket=memleket 
        
        
kisi1=Person("mert",24,"erkek","samsun")
kisi2=Person("zehra",11,"kız","Ardahan")
kisi3=Person("berkan",10,"erkek","samsun")

print (kisi2)
print(kisi2.yas)
print(kisi3.isim)


#öğrenci adında bir class oluşrurun içinde isim soy isim sınıf okul no olsun.
#nesne de oluiru en son ekran anesne nin ismini ve no yu yazdır


class Ogrenci :
    def __init__ (self,isim,soyisim,sınıf,okulno):
        self.isim=isim
        self.soyisim=soyisim
        self.sınıf=sınıf
        self.okulno=okulno 
        
        
ogrenci1=Ogrenci ("zehra","ertürk","6/E",569)

print ( ogrenci1.isim)
print ( ogrenci1.okulno)




#0541 361 42 46







