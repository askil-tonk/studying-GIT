import turtle
from math import *
from random import randrange
turtle.speed(0)
turtle.Screen().colormode(255)
turtle.Screen().bgcolor('black')
# turtle.Screen().tracer(25, 0)


def random_color():
    return randrange(256), randrange(256), randrange(256)


def star(side, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(side)
        turtle.right(144)
    turtle.end_fill()


def draw_star(x, y):
    turtle.goto(x, y)
    turtle.setheading(randrange(360))
    star(randrange(40, 100), random_color())


turtle.hideturtle()
turtle.up()
turtle.Screen().onclick(draw_star)
# draw_star()

turtle.Screen().mainloop()
