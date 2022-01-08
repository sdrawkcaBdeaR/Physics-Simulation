import turtle as tu

wn=tu.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)

scorea=0
scoreb=0

#paddle A for the left side 
pa=tu.Turtle()
pa.speed(0)
pa.shape("square")
pa.color("white")
pa.shapesize(stretch_wid=5,stretch_len=1)
pa.penup()
pa.goto(-350,0)

#paddle B for the right side 
pb=tu.Turtle()
pb.speed(0)
pb.shape("square")
pb.color("white")
pb.shapesize(stretch_wid=5,stretch_len=1)
pb.penup()
pb.goto(350,0)

#Ball for the game 
B=tu.Turtle()
B.speed(0)
B.shape("square")
B.color("white")
B.penup()
B.goto(0,0)
B.x=3
B.y=-3

pen=tu.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,265)

pen.write(("player A:{} player B:{}".format(scorea,scoreb)),align="center",font=("Courier",24,"normal"))


def pa_up ():
    pa.sety(pa.ycor()+10)

def pa_down ():
    pa.sety(pa.ycor()-10)

def pb_up ():
    pb.sety(pb.ycor()+10)

def pb_down ():
    pb.sety(pb.ycor()-10)

wn.listen()
wn.onkeypress(pa_up,"w")
wn.onkeypress(pa_down,"s")
wn.onkeypress(pb_up,"e")
wn.onkeypress(pb_down,"d")


while True:

    B.setx(B.xcor()+B.x)
    B.sety(B.ycor()+B.y)
    if B.ycor()>250:
        B.y*=-1
    if B.ycor()<-250:
        B.y*=-1 

    if pb.ycor()-50<B.ycor()<pb.ycor()+50 and B.xcor()>330:
            B.x*=-1    
    if pa.ycor()-50<B.ycor()<pa.ycor()+50 and B.xcor()<-330:
            B.x*=-1        

    if B.xcor()>350:
        B.goto(0,0)    
        B.x*=-1
        scorea+=1
        pen.clear()
        pen.write(("player A:{} player B:{}".format(scorea,scoreb)),align="center",font=("Courier",24,"normal"))

    if B.xcor()<-350:
        B.goto(0,0)     
        B.x*=-1
        scoreb+=1
        pen.clear()
        pen.write(("player A:{} player B:{}".format(scorea,scoreb)),align="center",font=("Courier",24,"normal"))


wn.mainloop()