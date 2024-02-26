#A-B aralığındaki sayıların toplamını ekrana yazan
#bir fonksiyon yazalım. Fonksiyon ismi a_plus_b
#olacaktır.
"""
def a_plus_b(a, b):
    return (a + b)

# Kullanım örneği
print(a_plus_b(3, 4))
"""


def a_plus_b(a, b):
    total = 0
    for i in range(a+1,b):
        total += i
    return total

# Kullanım örneği
print(a_plus_b(1,9))



#benim_sehrim adında bir fonksiyon oluşturun ve default bir şehir ismi giriniz

def benim_sehrim(sehir="Ankara"):
    print("Seçtiğiniz şehir:", sehir)

# Kullanıcıdan sehir ismi alma
sehir = input("Lütfen bir şehir ismi giriniz (varsa): ")

# Seçtiğiniz şehri göster
if sehir:
    benim_sehrim(sehir)
else:
    benim_sehrim()









