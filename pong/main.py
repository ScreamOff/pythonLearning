import turtle

wn = turtle.Screen()
wn.title("the game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

score_a = 0
score_b = 0
# paddleA
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350, 0)

# paddleB
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(350, 0)
# turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player a: 0 PlayerB: 0", align="center", font=("fixedsys", 24, "normal"))

endscor = turtle.Turtle()
endscor.speed(0)
endscor.color("white")
endscor.penup()
endscor.hideturtle()
endscor.goto(0, 0)


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
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


# klawiatura
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.xcor() < (-390):
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player a: {} PlayerB: {}".format(score_a, score_b), align="center", font=("fixedsys", 24, "normal"))
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player a: {} PlayerB: {}".format(score_a, score_b), align="center", font=("fixedsys", 24, "normal"))
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < (-290):
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -330 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
    elif ball.xcor() > 330 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1

    if score_a == 3:
        endscor.clear
        endscor.write("Player a wins", align="center", font=("fixedsys", 24, "normal"))
    elif score_b == 3:
        endscor.clear
        endscor.write("Player b wins", align="center", font=("fixedsys", 24, "normal"))
