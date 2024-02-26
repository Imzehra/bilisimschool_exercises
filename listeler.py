#LÄ°STELER
oyunlar = ["fortnite","minecraft","brwal stars","sims","valorant"]
print (oyunlar[3]) #oyunlar listesinin 3. indexini gÃ¶sterir.
oyunlar.append ("csgo") #listenin sonuna ekleme yapar.
print (oyunlar) 
#clear komutu listeyi remizler
#copy komutu listeyi kopyalar
say = oyunlar.count ("sims") #bir elamanÄ±n kaÃ§ tane olduÄunu sayar
print (say)

#extend komutu iki listeyi birbirine birleÅtirir.
print (oyunlar.index("valorant")) #index verinin kaÃ§Ä±ncÄ± sÄ±rarada olduÄunu belirler


oyunlar.insert (2,"fifa") #istenilen eyere eleman denir
print (oyunlar)

oyunlar.pop (2) #belirtilen index numarasÄ±ndaki veriyi siler
print (oyunlar)


oyunlar.remove ("fortnite") #belirtilen veriyi kaldÄ±rÄ±r.
print (oyunlar)

