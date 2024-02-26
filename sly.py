import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("green")

# Create a turtle
slytherin = turtle.Turtle()
slytherin.color("white")

# Draw the green background circle
slytherin.penup()
slytherin.goto(0, -150)
slytherin.pendown()
slytherin.circle(150)

# Draw the white snake head shape
slytherin.penup()
slytherin.goto(-20, 50)
slytherin.pendown()
slytherin.right(70)
slytherin.forward(100)
slytherin.right(110)
slytherin.forward(80)
slytherin.right(180)
slytherin.forward(40)
slytherin.right(70)
slytherin.forward(38)

# Add the text
slytherin.penup()
slytherin.goto(-85, 70)
slytherin.pendown()
slytherin.write("Slytherin", font=("Arial", 24, "normal"))

# Hide the turtle
slytherin.hideturtle()

# Keep the window open
turtle.done()
