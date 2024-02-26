import turtle 

t=turtle.Pen ()

def up ():
    t.fd (5)
    
    
def left ():
    t.left(5)
    
def right ():
    t.right (5)
    
def sil (): 
    t.color ("white")
    t.backward (5)
    t.color ("black")
     
def uc ():
    t.penup ()

def indir ():
    t.pendown ()

def doldur () :
    t.befin_fill ()
    
def birak ():
    t.end_fill ()
    
def daire ():
    yaricap= int(turtle.numinput("daire çapı","yarıçap giriniz."))
    t.circle(yaricap)
    
turtle.onkeypress(up,"Up")   
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.onkeypress (sil,"Down")  
turtle.onkeypress (uc,"u")
turtle.onkeypress (indir,"i")  
turtle.onkeypress (doldur,"d")
turtle.onkeypress(birak,"b")   
turtle.onkeypress (daire,"c")    
    
turtle.listen()    
    


















    
    