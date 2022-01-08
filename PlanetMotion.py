import turtle as tu
import math

wn=tu.Screen()
wn.bgcolor("black")
wn.title("Orbit")

tu.hideturtle()
tu.speed(0)

k=10

planet1=tu.Turtle()
planet1.penup()
planet1.shape("circle")
planet1.color("orange")
planet1.m=1
planet1.vx=-1.5
planet1.vy=0

planet2=tu.Turtle()
planet2.penup()
planet2.goto(150,150)
planet2.shape("circle")
planet2.color("red")
planet2.m=250
planet2.vx=1.5
planet2.vy=0

def force(p1,p2):
    dx=p1.xcor()-p2.xcor()
    dy=p1.ycor()-p2.ycor()
    r=math.sqrt((dx**2)+(dy**2))
    fx=k*p1.m*p2.m*dx/(r**3)
    fy=k*p1.m*p2.m*dy/(r**3)
    return fx,fy

while True:
    fx,fy=force(planet1,planet2)
    planet1.vx-=fx
    planet1.vy-=fy
    planet2.vx+=fx
    planet2.vy+=fy
    planet1.setx(planet1.xcor()+planet1.vx)
    planet1.sety(planet1.ycor()+planet1.vy)
    planet2.setx(planet2.xcor()+planet2.vx)
    planet2.sety(planet2.ycor()+planet2.vy)

wn.mainloop()