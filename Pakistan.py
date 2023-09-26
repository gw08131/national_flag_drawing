import turtle as t
from turtle import *

hideturtle()

speed(10)
setup(800, 500)
bgcolor("#01411C")

penup() 
goto(0, -100)
pendown()
color("#FFFFFF")
begin_fill()
circle(120)
end_fill()

penup()
goto(40, -65)
pendown()
color("#01411C")
begin_fill()
circle(120)
end_fill()


penup() #별
goto(40, 65)
pendown()

color("#FFFFFF") 
begin_fill()
n = 5
t.shape('turtle')
for i in range(n):
    t.forward(30)
    t.right((360 / n) * 2)
    t.forward(30)
    t.left(360 / n)
end_fill()
