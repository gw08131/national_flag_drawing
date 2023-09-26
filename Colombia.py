import turtle as t
from turtle import *

hideturtle()
def Draw(color, size):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(size*2)
    t.right(90)
    t.forward(size+50)
    t.right(90)
    t.forward(size*4)
    t.right(90)
    t.forward(size+50)
    t.right(90)
    t.end_fill()


speed(4)
setup(800, 500)
bgcolor("#FCD116")

Draw("#003893",200)

penup()
goto(0, -125)
pendown()
Draw("#CE1126",200)


