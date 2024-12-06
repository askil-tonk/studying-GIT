import turtle
from random import randrange
# turtle.Screen().colormode(255)
turtle.Screen().bgcolor('darkblue')

r = 100
turtle.hideturtle()
turtle.penup()
turtle.dot(r, 'orange')

shadow = turtle.Turtle()
shadow.hideturtle()
shadow.penup()
shadow.goto(r, 0)
shadow.shape('circle')
shadow.color('darkblue')
shadow.shapesize(r // 100 * 5)
shadow.showturtle()

for i in range(r, -r, -1):
    shadow.goto(i, 0)


turtle.Screen().mainloop()
