def gelismis_hesap_makinesi():
    while True:
        print("\nGelişmiş Hesap Makinesi Operasyonları:")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Hesap Makinesinden Çık")
        secim = input("Bir işlem seçiniz (1/2/3/4/5): ")
        if secim in ('1','2','3','4'):
            sayilar = input("Lütfen Sayıları Arasında Boşluk Bırakarak Giriniz. Örn(3 10 55):")
            sayi_listesi=[float(sayi) for sayi in sayilar.split()]
            if secim == '1':
                sonuc = sum(sayi_listesi)
            elif secim == '2':
                sonuc = sayi_listesi[0]
                for sayi in sayi_listesi[1:]:
                    sonuc -= sayi
            elif secim == '3':
                sonuc=1
                for sayi in sayi_listesi:
                    sonuc *= sayi
            elif secim == '4':
                sonuc = sayi_listesi[0]
                try:
                    for sayi in sayi_listesi[1:]:
                        sonuc /= sayi
                except ZeroDivisionError:
                    print("Hata! Bir sayı sıfıra bölünemez.")
                    continue
            print("SONUÇ:", sonuc)
        elif secim =='5':
            print("Hesap Makinesinden Çıkılıyor...")
            break
        else:
            print("Geçersiz Giriş!")
gelismis_hesap_makinesi()