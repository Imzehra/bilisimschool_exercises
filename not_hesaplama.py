notlar = {
    "mahmut": 85,
    "zehra": 100,
    "ada":59,
    "yağmur":100,
    "esma":100,
    "zeynep":100,
    "ipek":75,
}
harf_notu = {}
for element in notlar:
    harf_notu = notlar [element]
    if harf_notu > 90 :
        notlar[element] = "A"
    elif harf_notu >80:
        notlar[element] = "B"
    elif harf_notu >70:
        notlar[element] = "C"
    elif harf_notu >60:
        notlar[element] = "D"
    else:
        notlar[element]="F"
        
print (notlar)
        
    
    
