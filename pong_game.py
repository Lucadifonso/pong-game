import turtle #good for game without using PyGame
import os #needed to use sound

#WINDOW SETUP
wn = turtle.Screen()
wn.title("Pong by @Liucks")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #this stops the window from updating and we need to manual update it - makes the game faster

# SCORE
score_a = 0
score_b = 0

#PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #this is the speed of the animation not how fast the paddle moves
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() #Turtle by definition draw lines so we do a PenUp
paddle_a.goto(-350,0)

#PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #this is the speed of the animation not how fast the paddle moves
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup() #Turtle by definition draw lines so we do a PenUp
paddle_b.goto(350,0)

#BALL
ball = turtle.Turtle()
ball.speed(0) #this is the speed of the animation not how fast the paddle moves
ball.shape("square")
ball.color("white")
# no need to stretch
ball.penup() #Turtle by definition draw lines so we do a PenUp
ball.goto(0,0)
ball.dx = 0.5 #ball movement will be separated in two different direction dx and dy
ball.dy = 0.5


# Pen
pen = turtle.Turtle()
pen.speed(0) #animation speed, not the movement speed
pen.color("white")
pen.penup() #this remove the line between the points
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align= "center", font=("courier",24,"normal"))



#FUNCTION
def paddle_a_up():
    y = paddle_a.ycor() #.ycor is from turtle module and it returns the y coordinate and we assign it to a variable called Y
    y += 20 #this will add 20px to the y coordinate
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


#KEYBOARD BINDING
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#MAIN GAME LOOP
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #this line reverse the direction of the ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))


# Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
       
