# This is our project
import turtle
import random
import math

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

# лиса
pen.up()
pen.goto(-200,-100)
pen.down()
pen.width(5)
pen.color("orange")
# голова
pen.forward(120)
pen.right(180-45)
pen.forward(84.9)
pen.right(180-45)
pen.forward(120)
pen.left(180-45)
pen.forward(84.9)
pen.left(45)
pen.forward(60)
pen.left(90)
pen.forward(60)
# тело 1 нога
pen.right(180-45)
pen.forward(100)
pen.left(180-45)
pen.forward(math.sqrt(20000))
pen.left(180-45)
pen.forward(100)
pen.backward(60)
# 2 нога
pen.right(135)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(135)
pen.forward(141.4)
pen.right(135)
pen.forward(100)
# 3 нога
pen.right(45)
pen.forward(math.sqrt(65*65+65*65))
pen.right(135)
pen.forward(65)
pen.right(90)
pen.forward(65)
# хвост
pen.right(45)
pen.forward(40)
pen.right(45)
pen.forward(90)
pen.right(135)
pen.forward(40)
pen.right(45)
pen.forward(90)
# глаз
pen.up()
pen.width(6)
pen.color("red")
pen.goto(-200,-160)
pen.down()
pen.circle(3)
pen.left(90)
pen.up()
pen.forward(100)
pen.write("лиса", font=("Arial", 14, "bold") )

# дерево
pen.up()
pen.goto(-300,0)
pen.setheading(90)
pen.color("brown")
pen.down()
pen.begin_fill()
pen.forward(100)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(30)
pen.end_fill()
pen.right(90)
pen.forward(75)
pen.right(90)
pen.forward(15)
pen.begin_fill()
pen.color("green")
pen.circle(60)
pen.end_fill()
pen.left(90)
pen.forward(60)
pen.right(90)
pen.begin_fill()
pen.circle(50)
pen.end_fill()
pen.left(90)
pen.forward(70)
pen.right(90)
pen.begin_fill()
pen.circle(30)
pen.end_fill()






# then draw the triangle


 # then draw grass
"""
pen.color("green")
pen.width(2)

##
x=-270
y=-10
for counter in range(40):
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.setheading(90)
    pen.width(random.randint(1,3))
    pen.circle(  random.choice([-1,1]) * random.randint(100,130),     random.randint(10,20))
    x = x+random.randint(3,6)

"""

pen.screen.exitonclick()
