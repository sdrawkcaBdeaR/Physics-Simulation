import turtle as tu
import math as ma

yshift=200
g=0.5

wn=tu.Screen()
wn.title("DoublePendulum")
wn.bgcolor("black")
wn.setup(width=800,height=600)

#ball A for the left side 
pa=tu.Turtle()
pa.speed(0)
pa.shape("circle")
pa.color("white")
pa.shapesize(stretch_wid=1,stretch_len=1)
pa.x=0
pa.y=0
pa.length=100
pa.m=10
pa.theta=ma.pi/2
pa.omega=0
pa.angacc=0
pa.penup()


#ball B for the right side 
pb=tu.Turtle()
pb.speed(0)
pb.shape("circle")
pb.color("white")
pb.shapesize(stretch_wid=1,stretch_len=1)
pb.x=0
pb.y=0
pb.length=100
pb.m=10
pb.theta=ma.pi/2
pb.omega=0
pb.angacc=0
pb.penup()

la=tu.Turtle()
la.speed(0)
la.shape("square")
la.color("white")
la.shapesize(stretch_wid=5,stretch_len=0.5)
la.x=0
la.y=0
la.penup()

lb=tu.Turtle()
lb.speed(0)
lb.shape("square")
lb.color("white")
lb.shapesize(stretch_wid=5,stretch_len=0.5)
lb.x=0
lb.y=0
lb.penup()

la.left((180*pa.theta)/ma.pi)
lb.left((180*pb.theta)/ma.pi)

ba=(180*pa.theta)/ma.pi
bb=(180*pb.theta)/ma.pi


while True:
    pa.x=pa.length*ma.sin(pa.theta)
    pa.y=-pa.length*ma.cos(pa.theta)
    pb.x=pb.length*ma.sin(pb.theta)+pa.x
    pb.y=-pb.length*ma.cos(pb.theta)+pa.y

    num1=-g*(2*pa.m+pb.m)*ma.sin(pa.theta)
    num2=-g*pb.m*ma.sin(pa.theta-2*pb.theta)
    num3=-2*ma.sin(pa.theta-pb.theta)*pb.m
    num4=(pb.omega)*(pb.omega)*pb.length+(pa.omega)*(pa.omega)*pa.length*ma.cos(pa.theta-pb.theta)

    num5=2*ma.sin(pa.theta-pb.theta)
    num6=(pa.omega)*(pa.omega)*pa.length*(pa.m+pb.m)
    num7=g*(pa.m+pb.m)*ma.cos(pa.theta)
    num8=(pb.omega)*(pb.omega)*pb.length*pb.m*ma.cos(pa.theta-pb.theta)

    den=2*pa.m+pb.m-pb.m*ma.cos(2*(pa.theta-pb.theta))

    pa.angacc=(num1+num2+num3*num4)/(pa.length*den)
    pb.angacc=(num5*(num6+num7+num8))/(pb.length*den)

    pa.omega+=pa.angacc
    pb.omega+=pb.angacc

    pa.theta+=pa.omega
    pb.theta+=pb.omega

    la.goto(pa.x/2,yshift+pa.y/2)
    lb.goto(pb.x/2+pa.x/2,yshift+pb.y/2+pa.y/2)

    pa.goto(pa.x,yshift+pa.y)
    pb.goto(pb.x,yshift+pb.y)

    la.left(180*pa.theta/ma.pi-ba)
    ba=180*pa.theta/ma.pi

    lb.left(180*pb.theta/ma.pi-bb)
    bb=180*pb.theta/ma.pi

    pb.pendown()

wn.mainloop()