#turtle 
#Turtle modülü bir grafik mödülüdr. 

#Turtle grafikleri bir ekran üzerinde kaplumbağa gibi bir nesnenin hareket ettirilmesi ile oluşur

"""import turtle #modülü çağırdık
a = turtle.Turtle () # bir nesne oluşturduk
a.circle(100) # 50 yarı çaplı bir daire çiziyoruz 
turtle.getscreen() ._root.mainloop()"""

#a.forward (100) 100 birim ileri git
#a.backward (50) 50 birim geri git
#a.right (90) 90 derece sağa dön 
#a.left (45) 45 derece sola dön 
#a.penup () kalemi kaldır,çizmi durdurur
#a.pendown () kalemi indir,çizmi tekrar çizim yapar hale getirir.



#import turtle 
"""
y = turtle.Turtle ()
y.forward (100)

y.penup ()
y.forward (80)
y.pendown ()

y.forward (100)
"""

#a.pencolor("green")  çizginin rengini degistirir
#a.pensize (5) kalemin ucunu buyuttuk 

#a.goto (100,100)  ekranda 100,100 noktasına gider 

"""

z = turtle.Screen #çizim ekranı olsturur
d = turtle.Turtle (shape="turtle")  #nesne oluşturduk 

d.forward (100)
d.left (90)

d.forward (50)
d.left (90)

d.forward (100)
d.left (90)

d.forward (50)
"""

#shape parametresinin için arrow,turtle,circle,square,triangle,classic girebilirsiniz


"""
d = turtle.Turtle (shape = "turtle")

d.begin_fill()  #çizilen nesnein içerisini doldurur.

d.color ("green")
d.circle (150)
d.end_fill ()  #içini  doldurma işlemini bitirir

d.begin_fill ()
d.color ("grey")
d.circle (75)
d.end_fill () 

"""

from turtle import Screen,Turtle 
from random import random

radius = 200 #dairenin yarı çapı 

screen=Screen ()
turtle = Turtle ()
turtle.shape ("turtle")
turtle.shapesize (5,outline=5)
turtle.speed ("fast")
turtle.width (90)

turtle.penup ()
turtle.sety (-radius) # ekranın tam ortasında olmasi
turtle.pendown ()



def randomize () :
    turtle.pencolor (random(),random(),random())
    turtle.fillcolor (random(),random(),random())
    
    turtle.circle(radius,extent=30)
    screen.ontimer(randomize)
    
randomize ()

screen.exitentclick ()
















