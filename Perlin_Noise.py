#import libraries
import random as ra
import turtle
pr,pg,pb=100,100,100
wid=1376
y=wid/2*-1
asp=10
#create turtle
s=turtle.getscreen()
screen=turtle.Screen()
screen.colormode(255)
#makes two circle turtles
tc1=turtle.Turtle()
tc1.pensize(15)
tc1.speed(0)
tc2=turtle.Turtle()
tc2.pensize(15)
tc2.speed(0)
#turtle num 1
t1=turtle.Turtle()
t1.speed(0)
t1.penup()
t1.goto(y,0)
t1.pencolor("blue")
#turtle num #2
t2=turtle.Turtle()
t2.speed(0)
t2.penup()
t2.goto(y,0)
t2.pencolor("green")
#turtle num #3
t3=turtle.Turtle()
t3.speed(0)
t3.penup()
t3.goto(y,0)
t3.pencolor("red")
#def noise
def noise(av,cm,asp,prev=None):
    #assigns prev a value if no value is avaible
    if prev==None:
        prev=av
    #set x to true
    x=True
    #will run untill awnser is within acseptible limits
    while x==True:
        #makeing a varible be a random number
        h=av+ra.randrange((-1*cm),cm)
        #making sure that number is within accsepticle limits
        if h-asp>prev or h+asp<prev:
            x=True
        #will stop code and return h // the value
        else:
            x=False
            return int(h)
while y<wid/2:
    #thing one
    b=noise(100,100,asp,pb)
    pb=b
    t1.goto(y,b-85)
    t1.pendown()  
    #thing two
    g=noise(100,100,asp,pg)
    pg=g
    t2.goto(y,g-85)
    t2.pendown()
    #thing three
    r=noise(100,100,asp,pr)
    pr=r
    t3.goto(y,r-85)
    t3.pendown()
    #main circle
    if y%2!=0:
        tc1.pencolor(r,g,b)
        tc1.circle(30)
        tc2.clear()
    else:
        tc2.pencolor(r,g,b)
        tc2.circle(30)
        tc1.clear()
    y+=1
screen.exitonclick()