
"""from turtle import Turtle,Screen 

y = Turtle()

kenar_sayisi = 5

for a in range (kenar_sayisi):
    ac = 360 / kenar_sayisi
    y.forward(50)
    y.right(ac)

my_screen = Screen ()
my_screen.exitonclick
"""
from turtle import Turtle,Screen

my_screen = Screen ()
my_screen.exitonclick
y = Turtle()

def s (kenar_sayisi):
    ac = 360 / kenar_sayisi
    for a in range (kenar_sayisi):
        y.forward(50)
        y.right(ac)
for e in range (4,10):
    sekil_ciz (e)













