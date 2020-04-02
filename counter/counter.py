import turtle

wn = turtle.Screen()
wn.title("counter")
wn.bgcolor("black")
wn.setup(width=200, height=300)
wn.tracer(0)
a = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.write(a, align="center", font=("fixedsys", 24, "normal"))


def counter_up():
    global a
    a += 1
def counter_down():
    global a
    a -= 1


wn.listen()
wn.onkeypress(counter_up, "w")
wn.onkeypress(counter_down,"s")

while True:
    wn.update()
    pen.clear()
    pen.write(a, align="center", font=("fixedsys", 24, "normal"))
