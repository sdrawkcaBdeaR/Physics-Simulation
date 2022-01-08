import turtle as tu
import math

wn=tu.Screen()
wn.bgcolor("black")
wn.title("Orbit")

tu.speed(0)

n=3
k=100
planet=[]

for _ in range(n):
    planet.append(tu.Turtle())

def create (p,m,vx,vy,x,y,col):
    #p.penup()
    p.goto(x,y)
    p.shape("circle")
    p.color(col)
    p.m=m
    p.vx=vx
    p.vy=vy

create(planet[0],1,1,-1,0,0,"red")
create(planet[1],10,0,1,150,150,"orange")
create(planet[2],1,0,1,-150,-150,"yellow")

def force(p1,p2):
    dx=p1.xcor()-p2.xcor()
    dy=p1.ycor()-p2.ycor()
    r=math.sqrt((dx**2)+(dy**2))
    fx=k*p1.m*p2.m*dx/(r**3)
    fy=k*p1.m*p2.m*dy/(r**3)
    return fx,fy

while True:
    for i in range(n):
        for j in range(n):
            if i!=j :
                fx,fy=force(planet[i],planet[j])
                planet[i].vx-=fx
                planet[i].vy-=fy

    for i in range(n):    
        planet[i].setx(planet[i].xcor()+planet[i].vx)
        planet[i].sety(planet[i].ycor()+planet[i].vy)


wn.mainloop()