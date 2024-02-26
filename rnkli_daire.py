import turtle
import random 

t=turtle.Pen()
t.speed(0)
turtle.bgcolor ("black")
renk = ["red","green","pink","purple","blue","yellow","grey"]

def dongu (x,y):
    t.color (random.choice(renk))
    t.begin_fill ()
    size=random.randint(10,100)
    t.penup()
    t.setpos (x,y)
    t.pendown ()
    t.circle(size)
    t.end_fill ()

turtle.onscreenclick (dongu)






































