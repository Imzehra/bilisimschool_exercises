
"""import turtle 

def git (x,y) :
    turtle.goto (x,y)
    
turtle.listen()
turtle.onscreenclick(git)
turtle.mainlop()
"""
def check_sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0
num = float(input("Enter a number: "))
print(check_sign(num))
    
    
    
    
    