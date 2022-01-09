import turtle as tu

wn=tu.Screen()
wn.bgcolor("black")
wn.title("collisions")

collisions=0
n=2

tu.penup()
tu.hideturtle()
tu.pensize(2)
tu.color("white")
tu.goto(-12,40)
tu.pendown()
tu.goto(-12,-12)
tu.goto(500,-12)
tu.penup()

a=tu.Turtle()
a.shape("square")
a.penup()
a.speed(0)
a.color("blue")
a.goto(200,0)
a.m=1
a.v=0

b=tu.Turtle()
b.shape("square")
b.penup()
b.speed(0)
b.color("red")
b.goto(300,0)
b.m=100**n
b.v=-0.2

pen=tu.Turtle()
pen.penup()
pen.color("white")
pen.hideturtle()
pen.speed(0)
pen.goto(0,250)
pen.write("Collisions:{}".format(collisions),align="center",font=("Courier",24,"normal"))

while True:
    b.setx(b.xcor()+b.v)
    a.setx(a.xcor()+a.v)

    if (b.xcor()-a.xcor())<20:
        collisions+=1
        n=(2*b.m*b.v)/(b.m+a.m)-((b.m-a.m)*a.v)/(b.m+a.m)
        m=(2*a.m*a.v)/(b.m+a.m)+((b.m-a.m)*b.v)/(b.m+a.m)
        a.v=n
        b.v=m
        pen.clear()
        pen.write("Collisions:{}".format(collisions),align="center",font=("Courier",24,"normal"))


    if a.xcor()<0:
        collisions+=1
        a.v*=-1
        pen.clear()
        pen.write("Collisions:{}".format(collisions),align="center",font=("Courier",24,"normal"))

wn.mainloop()    