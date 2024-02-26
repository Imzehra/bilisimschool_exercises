import random
import turtle

screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("DÜŞEN HARFLER ")
screen.bgcolor ("lightgreen")
screen.tracer(0,0) #ekran akısının surekli devam etmesini ve rastgele dusmesini istiyoruz
turtle.hideturtle ()
turtle.up()
turtle.color("black")

score_turtle = turtle.Turtle ()
score_turtle.color("neonpink")
score_turtle.up ()
score_turtle.hideturtle ()
turtle.goto(350,400)
turtle.write("Score ",align="center",font=("Arial",30,"normal"))

min_speed = 1
max_speed=5
letters=[]
speeds = []
pos =[]
lts =[]
n=5 # baslangıc harf sayısı
game_over = False
score = 0

def increase_difficulty () :
    global min_speed , max_speed
    min_speed +=1
    max_speed +=1
    screen.ontimer(increase_difficulty, 10000)

def draw_game_over ():
    turtle.goto (0,0)
    turtle.color("red")
    turtle.write("OYUN BİTTİ!!!!!!",align="center",font =("Arial",50,"normal","bold"))

    turtle.goto(0,-150)
    turtle.color("darkorange")
    turtle.write("skorun {}".format(score),align="center",font("Courier",40,"normal"))
    screen.update()

def draw_score ():
    score_turtle.clear()
    score_turtle.goto(420,400)
    score_turtle.write ( {}.format(score),align="center",font("Courier",25,"normal"))
    screen.update ()

def draw_letters ():
    global game_over
    for i in range (len(letters)):
        lts[i].clear ()
        lts[i].goto(pos[i]
        lts[i].write(letters[i],align="center",font=("Courier",20,"normal"))
        pos[i] [1] -=speeds[i]
        if pos[i][1]<-500:
            game_over = True
            draw_game_over ()
            return
    screen.update ()
    screen.ontimer(draw_letters,50)

def f(c): # klavyeye basma fonksiyonumuz
    global score
    if c in letters:
        score += 1
        k = letters.index(c)
        while True:
            l = chr(ord('a')+random.randrange(26))
            if l not in letters:
                letters[k] = l
                break            
        pos[k] = [random.randint(-450,450),500]        
        speeds[k] = random.randint(min_speed,max_speed)
    else: score -= 1
    draw_score()
        
for _ in range(n):
    lts.append(turtle.Turtle())
    while True:
        l = chr(ord('a')+random.randrange(26))
        if l not in letters:
            letters.append(l)
            break
    speeds.append(random.randint(min_speed,max_speed))
    pos.append([random.randint(-450,450),500])

for i in range (n):
    lts[i].speed(0)
    lts[i].hideturtle ()
    lts[i].up ()
    lts[i].color("black")
    lts[i].write(letters[i],align="center",font("Arial",20,"normal","bold"))

draw_letters ()
increase_difficulty ()
screen.onkey(lambda:f("a"),"a")
screen.onkey(lambda:f("b"),"b")
screen.onkey(lambda:f("c"),"c")
screen.onkey(lambda:f("d"),"d")
screen.onkey(lambda:f("e"),"e")
screen.onkey(lambda:f("g"),"g")
screen.onkey(lambda:f("h"),"h")
screen.onkey(lambda:f("ı"),"ı")
screen.onkey(lambda:f("i"),"i")
screen.onkey(lambda:f("j"),"j")
screen.onkey(lambda:f("k"),"k")
screen.onkey(lambda:f("l"),"l")
screen.onkey(lambda:f("m"),"m")
screen.onkey(lambda:f("n"),"n")
screen.onkey(lambda:f("o"),"o")
screen.onkey(lambda:f("ö"),"ö")
screen.onkey(lambda:f("p"),"p")
screen.onkey(lambda:f("r"),"r")
screen.onkey(lambda:f("s"),"s")
screen.onkey(lambda:f("ş"),"ş")
screen.onkey(lambda:f("t"),"t")
screen.onkey(lambda:f("u"),"u")
screen.onkey(lambda:f("ü"),"ü")
screen.onkey(lambda:f("v"),"v")
screen.onkey(lambda:f("y"),"y")
screen.onkey(lambda:f("z"),"z")
screen.onkey(lambda:f("x"),"x")
screen.onkey(lambda:f("w"),"w")

screen.listen ()
screen.mainloop ()





























