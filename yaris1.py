from turtle import *
from random import randint

red = Turtle ()
red.color ("red")
red.shape ("turtle")
red.penup()
red.goto(-320,100)
red.pendown()

blue = Turtle ()
blue.color ("blue")
blue.shape ("turtle")
blue.penup ()
blue.goto(-320,-100)
blue.pendown ()

def yarispisti ():
    for x in range(31):
        write(x,align="center")
        right(90)
        for num in range (13):
            penup()
            forward(10)
            pendown()
            forward (10)
        penup()
        backward(260)
        left(90)
        forward(20)

def kazanan (kim):
    goto(-100,200)
    kazanan=kim+ "  kazandı!!!!  "
    pencolor(kim)
    write(kazanan,align="center",font=("Arial",40,"bold"))

speed(0)  #başlangıç hızları
penup()
goto (-290,130) #başlangıca gidilir
yarispisti() 


while (red.xcor()<310 and blue.xcor()<310):
    red.fd(randint(1,5))
    blue.fd(randint(1,5))  #kaplumbagalara rastgele hız verir


if (red.xcor()>=310):
    kazanan("red")

else :
    kazanan ("blue")
                                       
        






























