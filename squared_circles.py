from turtle import Turtle
from turtle import Screen
import math

t = Turtle()
screen = Screen()

def drawSquare(x,y,l):
    t.pu()
    t.home()
    t.goto(x,y-l)
    t.pd()
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(l)

def drawCircle(x,y,r):
    t.pu()
    t.goto(x,y-r)
    t.pd()
    t.circle(r)

def drawTriangle(x,y,l):
    t.pu()
    t.goto(x,y-l)
    t.pd()
    t.right(90)
    t.forward(l)
    t.left(120)
    t.forward(l)
    t.left(120)
    t.forward(l)

def squaredCircle(r,i,depth = 0):
    p = r*2*(1+2/math.sqrt(3))
    pi = math.pi
    print(depth)
    if(depth==0):
        drawCircle(0,0,r)
        drawSquare(-r,r*3,r*2)
        drawTriangle(-p/2,r*3.333,p)
    else:
        drawSquare(-r,r*pi,r*2)
        drawTriangle(-p/2,r*3.444+(depth/10),p)
    drawCircle(-p/2,r*2.5*1.6444,r*2.5)
    

    i=i-1
    if(i<=0):
        return
    squaredCircle(r*2.5,i,depth=depth+1)
    
while(True):
    squaredCircle(30,3)
    screen.exitonclick()






