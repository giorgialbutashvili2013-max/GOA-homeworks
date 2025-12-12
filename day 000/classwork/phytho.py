

from turtle import *

speed(100)


forward(200)
left(90)
forward(250)
left(90)
forward(200)
left(90)
forward(250)
left(90)

# კარი
forward(70)
left(90)
forward(100)
right(90)
forward(75)
right(90)
forward(100)

# სახელური
right(180)
forward(50)
left(90)
forward(15)
backward(15)
right(90)
backward(50)


penup()
goto(0, 250)        
pendown()
color("red")
begin_fill()
goto(100, 350)      
goto(200, 250)      
goto(0, 250)      
end_fill()


penup()
goto(30, 150)
pendown()
color("blue")
begin_fill()
setheading(0)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()

color("black")
forward(20)
left(90)
forward(40)
backward(20)
left(90)
forward(20)
backward(40)


penup()
goto(130, 150)
pendown()
color("blue")
begin_fill()
setheading(0)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()


color("black")
forward(20)
left(90)
forward(40)
backward(20)
left(90)
forward(20)
backward(40)

exitonclick()

