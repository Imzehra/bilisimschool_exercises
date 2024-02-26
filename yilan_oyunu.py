from turtle import Screen,Turtle
import time 

screen=Screen ()
screen.setup  = (600,600)
screen.bgcolor("green")
screen.title ("Yılan Oyunu")
screen.tracer (0)

pozisyonlar = [(0,0),(-20,0),(-40,0)]

parcalar = []

for pozisyon in pozisyonlar:
    body = Turtle(shape="square")
    body.penup ()
    body.goto(pozisyon)
    parcalar.append(body)



oyun = True
while oyun:
    screen.update ()
    time.sleep(0.1)
    """for parca in parcalar :
        parca.forward(20)"""
    for element in range (len(percalar) -1,0,-1):
        x = parcalar[element -1].xcor()
        y = parcalar [element -1].ycor()
        parcalar [element].goto(x,y)
    parcalar[0].forward(20)
    parcalar[0].left(90)
        




screen.exitonclick ()






























