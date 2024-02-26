bagis = {}

bagis_bitti = False 


def rekortmen_bul(bagis_kayit):
    en_yuksek_bagis = 0
    kazanan = ""
    for element in bagis_kayit:
        bagis_miktari = bagis_kayit[element]
        if bagis_miktari > en_yuksek_bagis:
            en_yuksek_bagis = bagis_miktari
            kazanan = element
    print(f'Kazanan ${en_yuksek_bagis} ile {kazanan}')
while not bagis_bitti:
    isim = input ("isim: ")
    bagis_miktarı = int (input ("bağış miktarı:  $"))
    bagis[isim] = bagis_miktarı
    bagis_devam = input ("Başka bağış verecek varmı? evet ya da hayır:")
   
    if bagis_devam=="hayır":
        bagis_bitti= True
        rekortmen_bul (bagis)
    elif bagis_devam == "evet":
        print ("\014")
       # print("isim: ")
        






















