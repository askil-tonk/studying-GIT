import turtle
from random import randrange
turtle.speed(0)
turtle.Screen().colormode(255)
turtle.Screen().bgcolor('black')


turtle.Screen().tracer(25, 0)


colors = ['green', 'yellow', 'red']


def random_color():
    return randrange(256), randrange(256), randrange(256)


def random_xy():
    side = 350
    return randrange(-side, side), randrange(-side, side)


def triangle(side, to_fill=False, color=None):
    if to_fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)
    if to_fill:
        turtle.end_fill()


def triangle_invert(side, to_fill=False, color=None):
    if to_fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    for _ in range(3):
        turtle.forward(side)
        turtle.right(120)
    if to_fill:
        turtle.end_fill()


def rectangle(width, heigth, to_fill=False, color=None):
    sides = [width, heigth, width, heigth]
    if to_fill:
        turtle.fillcolor(color)
        turtle.begin_fill()
    for side in sides:
        turtle.forward(side)
        turtle.left(90)
    if to_fill:
        turtle.end_fill()


def hexagon(side):
    for _ in range(6):
        for _ in range(7):
            turtle.forward(side)
            turtle.left(60)
#         turtle.right(120)

# triangle(150)
# turtle.penup()
# turtle.goto(0, 85)
# for _ in range(3):
#     turtle.dot(30, 'black')
#     turtle.forward(150)
#     turtle.right(120)
# triangle_invert(150, True, 'white')


def rainbow(rad, iter):
    dif = rad // iter
    turtle.penup()
    for i in range(iter):
        print(rad)
        turtle.dot(rad, random_color())
        rad -= dif


def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.pencolor('yellow')
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.speed(0)


def star(side, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(side)
        turtle.right(144)
    turtle.end_fill()


turtle.hideturtle()
turtle.penup()
for _ in range(100):
    turtle.goto(random_xy())
    turtle.setheading(randrange(360))
    star(randrange(10, 40), random_color())


turtle.Screen().mainloop()
