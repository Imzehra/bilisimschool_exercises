# İLERİ SEVİYE VERİ YAPILARI 

#SET VERİ TİPİ
#set veeri tipinfe elemanlar listelenmezler 
#listelenmedikleri için index numaraları yoktur
#dolayısıyla listeyi çağırdığımız zaaman her bir elemanın
#yeri farklı gelir 
#tekrarlanamazlar her elemandan bir tane olmalı
#{} parantez kullanılır 

set_liste = {1,2,3,4,5}
print (6 in set_liste) #in ile listenin aranan eleman
#SONUÇ:False //////varmı diye kontrol eder 
set_liste.add (6) #.add komutuyla istenilen eleman
print (set_liste) #listeye konur 
print (6 in set_liste)
set_liste.update ([7,8,9]) #listeye 1den fazla elmn ekler
print (set_liste)

set_liste.remove (6) #listeden eleman sileriz
print (set_liste)


































