import turtle
wndw = turtle.Screen()
wndw.title("Python Türk Bayrağı")
wndw.setup(720, 420)
wndw.bgcolor("Red")
kalem = turtle.Turtle()
### İlk Daire
kalem.color("White")
kalem.penup()
kalem.goto(-120, -100)
kalem.pendown()
kalem.begin_fill()
kalem.circle(120)
kalem.end_fill()
kalem.color("Red")
kalem.penup()
kalem.goto(-90, -80)
kalem.pendown()
kalem.begin_fill()
kalem.circle(100)
kalem.end_fill()
kalem.color("White")
kalem.penup()
kalem.goto(-30, 20)
kalem.pendown()
kalem.begin_fill()
kalem.left(10)
for i in range(5):
    kalem.forward(120)
    kalem.right(144)
kalem.end_fill()
### Çizim Sonu
kalem.hideturtle()
turtle.done()
