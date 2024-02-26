from turtle import *
from random import randint

#yarısacak olan kaplumbagaların renkleri
colors = ["red","blue","green","yellow","pink","purple"]

#kullanıcıdan tahmin alak
user_guess = textinput("tahmin","sence hangi renk kazanacak?(red,blue,yelllow,pink,purple)")

#keplumbişleri ve pozisyonları
turtles = []
for i in range (6):
    t = Turtle ()
    t.color(colors[i])
    t.shape ("turtle")
    t.penup ()
    t.goto (-320,(100-40*i))
    turtles.append(t)



#bitiş çizgisi
penup()
goto (250,150)
pendown()
pencolor("black")
pensize (10)
right(90)
forward(300)
penup ()
    
#yarışı başlatma
winning_color = None
while winning_color is None :
    for t in  turtles :
        t.fd(randint(1,5))
        if t.xcor() >=250:
            winning_color = t.color () [0]
            break

#kazanan rangi ekrana yazdır tahmini konrtol et
penup ()
goto (-200,0)
pencolor("brown")
if user_guess.lower()==winning_color :
    write (f"Tebrikler,doğru tahmin ettiniz kazanan renk : {winning_color}", align = "center",font = ("Arial",18,"bold"))
else :
    write(f"yanlış kazanan renk : {winning_color}", align = "center",font = ("Arial",18,"bold"))

done ()




















                       
