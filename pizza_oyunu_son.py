import random 

def kelime_sec():
    kelime_listesi = ["Can I have Hawaiian pizza? (hawaii pizzası alabilir miyim?)", 
                      "안녕하세요, 마가리타 하나 드실 수 있나요?(merhaba bir margarita alabilir miyim ?)", 
                      "Merhaba bir sucuklu lütfen!"]
    return random.choice(kelime_listesi)

print(kelime_sec())

liste1 = ["paket pizza hamuru",
          "domates sosu",
          "mozzarella peyniri",
          "ananas",
          "jambon",
          "220.00 TL"]

liste2 = ["domates",
          "mozarella",
          "fesleğen",
          "zeytinyağı",
          "tuz",
          "150,00 TL"]

liste3 = ["mozzarella peyniri",
          "zeytin",
          "marine mantar",
          "sucuk",
          "kırmızı ve yeşil biber",
          "360.00 TL"]

oyun_resim = [liste1, liste2, liste3]

kullanici_secimi = int(input("Hangisini seçiyorsunuz? \n0 - Hawaii Pizza, \n1 - Margarita, \n2 - Sucuklu\n"))

if kullanici_secimi >= 3 or kullanici_secimi < 0:
    print("Lütfen listemizde bulunan pizzalardan seçim yapınız.")
else:
    print(f""" Pizza İçeriğiniz ve fiyatı:
          {oyun_resim[kullanici_secimi]} """)
    print("Siparişiniz için teşekkür ederiz! Pizzanız yakında hazır olacak.")
