import turtle

wn = turtle.Screen()
wn.title("BMO")
wn.bgcolor("black")
wn.setup(width=1000, height=1000)
wn.tracer(0)

score = 0

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

paddle = turtle.Turtle()
paddle.speed(0)
paddle.penup()
paddle.goto(0, -400)
paddle.shape("square")
paddle.color("green")
paddle.shapesize(stretch_wid=1, stretch_len=5)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(-450, -300)
pen.write(score, align="center", font=("fixedsys", 24, "normal"))

start_x = -260
start_y = 450

length_x = 73
length_y = 33
kappa = 1
begin_x_value = []
begin_y_value = []

tab = []


def create_block(offset_x=0, offset_y=0):
    space0 = turtle.Turtle()
    space0.speed(0)
    space0.goto(start_x + (length_x * offset_x), start_y - (length_y * offset_y))
    space0.color("yellow")
    space0.shape("square")
    space0.shapesize(stretch_wid=1, stretch_len=3)
    begin_x_value.append(space0.xcor())
    begin_y_value.append(space0.ycor())
    return space0


def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 30 and abs(a.ycor() - b.ycor()) < 30
def paddlecolision(a, b):
    return abs(a.xcor() - b.xcor()) < 30 and abs(a.ycor() - b.ycor()) < 40


def create_blocks():
    for i in range(8):
        row = []
        for j in range(8):
            row.append(create_block(i, j))
        tab.append(row)


def find_possible_column(ball_x):
    for i in range(8):
        if (list(set(begin_x_value))[i] >= ball_x):
            return i


def paddle_right():
    x = paddle.xcor()
    x = x + 20
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    x = x - 20
    paddle.setx(x)


create_blocks()

wn.listen()
wn.onkeypress(paddle_left, "Left")
wn.onkeypress(paddle_right, "Right")
# mainloop
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][j] != None and is_collided_with(ball, tab[i][j]):
                tab[i][j].setx(10000000000000000)
                ball.dy *= -1
                ball.dx *= -1
                score+=1
    if kappa ==1:
        pen.clear()
        pen.write(score, align="center", font=("fixedsys", 24, "normal"))


    # krawedzie
    if ball.xcor() >= 290:
        ball.dx *= -1
    if ball.ycor() >= 500:
        ball.dy *= -1
    if ball.ycor() <= -500:
        ball.dy *= -1
    if ball.xcor() <= -290:
        ball.dx *= -1
    # odbicie
    if paddlecolision(paddle,ball):
        ball.dy *= -1
        ball.dx *= -1
    # ending
    if ball.ycor() <= -490:
        kappa = 0
        pen.clear()
        pen.goto(0, 0)
        pen.write("KONIEC GRY \nSCORE :{}".format(score), align="center", font=("fixedsys", 24, "normal"))
        ball.goto(0, 0)
        ball.color("yellow")
        ball.dx = 0.5
        ball.dy = 0.5
