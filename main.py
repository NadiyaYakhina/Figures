# This is our project
import turtle
# wn = turtle.Screen()
# wn.title("My Turtle")
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


pen.screen.exitonclick()
