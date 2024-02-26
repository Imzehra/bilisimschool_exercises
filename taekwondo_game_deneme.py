#TAEKWONDO GAME 

class DaTaTakwondoYapimi:
    def __init__(self):
        self.da_ta_takwondo_listesi = []

    def da_ta_takwondo_ekle(self,no,isim,yil,derece,cinsiyet):
        yeni_da_ta_takwondo = {
            'no': no,
            'isim': isim,
            'yil': yil,
            'derece': derece,
            'cinsiyet': cinsiyet
        }
        self.da_ta_takwondo_listesi.append(yeni_da_ta_takwondo)

    def da_ta_takwondo_listele(self):
        for da_ta_takwondo in self.da_ta_takwondo_listesi:
            print(f"No: {da_ta_takwondo['no']} İsim: {da_ta_takwondo['isim']} Yıl: {da_ta_takwondo['yil']} Derece: {da_ta_takwondo['derece']} Cinsiyet: {da_ta_takwondo['cinsiyet']}")

    def da_ta_takwondo_sil(self, no):
        for da_ta_takwondo in self.da_ta_takwondo_listesi:
            if da_ta_takwondo['no'] == no:
                self.da_ta_takwondo_listesi.remove(da_ta_takwondo)
                break

    def da_ta_takwondo_ara(self, no):
        for da_ta_takwondo in self.da_ta_takwondo_listesi:
            if da_ta_takwondo['no'] == no:
                print(f"No: {da_ta_takwondo['no']} İsim: {da_ta_takwondo['isim']} Yıl: {da_ta_takwondo['yil']} Derece: {da_ta_takwondo['derece']} Cinsiyet: {da_ta_takwondo['cinsiyet']}")
                break
        else:
            print(f"No: {no} olan da ta takwondo bulunamadı.")

    def da_ta_takwondo_guncellenecek_kisi_ara(self, no):
        for da_ta_takwondo in self.da_ta_takwondo_listesi:
            if da_ta_takwondo['no'] == no:
                return da_ta_takwondo
        else:
            return None

    def da_ta_takwondo_guncellenecek_kisi_sil(self, no):
        for da_ta_takwondo in self.da_ta_takwondo_listesi:
            if da_ta_takwondo['no'] == no:
                self.da_ta_takwondo_listesi.remove(da_ta_takwondo)
                break

    def da_ta_takwondo_guncellenecek_kisi_ekle(self, no, isim, yil, derece, cinsiyet):
        yeni_da_ta_takwondo = {
            'no': no,
            'isim': isim,
            'yil': yil,
            'derece': derece,
            'cinsiyet': cinsiyet
        }
        self.da_ta_takwondo_listesi.append(yeni_da_ta_takwondo)

da_ta_takwondo_yapimi = DaTaTakwondoYapimi()
da_ta_takwondo_yapimi.da_ta_takwondo_ekle(1, "Zehra", 2012,"birinci Derece", "kız")
    

