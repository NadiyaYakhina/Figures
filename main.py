# This is our project
import turtle
import random

pen = turtle.Turtle()
pen.screen.title("My Turtle 2")

# начинаем рисовать тут

# lets draw square
pen.width(7)
pen.color("brown")
pen.forward(150)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(150)
# окно
pen.up()
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.down()

pen.color("orange")
pen.forward(50)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(25)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(25)
pen.right(90)
pen.forward(25)
pen.right(90)
pen.forward(50)
pen.up()
pen.forward(50)
pen.right(90)
pen.forward(75)
pen.left(135)
# крыша
pen.down()
pen.color("red")
pen.begin_fill()
pen.fillcolor("red")
pen.forward(106)
pen.left(90)
pen.forward(106)
pen.left(180-45)
pen.forward(150)
pen.end_fill()

# then draw the triangle

# then draw spiral
pen.up();
pen.goto(-200,-50)
pen.color("green")
pen.width(2)
pen.left(90)


##
x=-200
for i in range(50):
    pen.down()
    pen.setheading(90)
    pen.width(random.randint(1,2))
    pen.circle(random.choice([-1,1])*random.randint(200,230),random.randint(20,30))
    pen.up()
    pen.goto(x, -50)
    x = x+random.randint(3,6)
    print(i)
    ##

pen.screen.exitonclick()
