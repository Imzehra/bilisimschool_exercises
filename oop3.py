class Ogrenci :
    def __init__ (self,isim,soyisim,sınıf,okul_no):
        self.isim=isim
        self.soyisim=soyisim
        self.sınıf=sınıf
        self.okul_no=okul_no 
        
        
    def Talk (self):
        print (f"""Benim adım soyadım {self.isim} {self.soyisim}.
               {self.sınıf}. sınıfa gidiyorum.
               okul numaram {self.okul_no}""")
        
ogrenci1=Ogrenci ("zehra","ertürk","6/E",569)

print (ogrenci1.isim)
print (ogrenci1.okul_no)
ogrenci1.Talk()
