# This is our project
import turtle
import random
import math


pen = turtle.Turtle()
pen.screen.title("My Turtle 2")
# подготовка ручки. перемещение в заданую позицию и установка увета и ширины
def prepare(x, y, color, width):
    pen.up()
    pen.goto(x, y)
    pen.setheading(0)
    pen.down()
    pen.width(width)
    pen.color(color)

# квадрат
def square(x, y, size, color="black", width=7):
    prepare(x, y, color, width)
    pen.forward(size)
    pen.left(90)
    pen.forward(size)
    pen.left(90)
    pen.forward(size)
    pen.left(90)
    pen.forward(size)


# равнобедренный треугольник
def equiTriangle(x, y, size, orientation, color="black", width=7):
    prepare(x, y, color, width)
    pen.begin_fill()
    pen.fillcolor(color)
    pen.right(orientation)
    pen.forward(size)
    pen.right(120)
    pen.forward(size)
    pen.right(120)
    pen.forward(size)
    pen.end_fill()

# дом
def house(x, y, size, colorWall, colorRoof):
    square(x, y, size, colorWall)
    windowSize = size/4
    windowX =  x + size/2 - windowSize/2
    windowY =  y + size/2 - windowSize/2
    square(windowX, windowY, windowSize, colorWall)
    equiTriangle(x+size/2, y+size+size, size+size/3, 60, colorRoof)

# старый дом
def oldHouse():
    prepare(0, 0, "brown", 7)
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
    pen.left(180 - 45)
    pen.forward(150)
    pen.end_fill()

# лиса
def fox(x, y, color="black", width=7):
    # лиса
    prepare(x, y, color, width)
    pen.goto(x, y)
    # голова
    pen.forward(120)
    pen.right(180 - 45)
    pen.forward(84.9)
    pen.right(180 - 45)
    pen.forward(120)
    pen.left(180 - 45)
    pen.forward(84.9)
    pen.left(45)
    pen.forward(60)
    pen.left(90)
    pen.forward(60)
    # тело 1 нога
    pen.right(180 - 45)
    pen.forward(100)
    pen.left(180 - 45)
    pen.forward(math.sqrt(20000))
    pen.left(180 - 45)
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
    pen.forward(math.sqrt(65 * 65 + 65 * 65))
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
    pen.goto(x, y-60)
    pen.down()
    pen.circle(3)
    pen.left(90)
    pen.up()
    pen.forward(100)
    # pen.write("лиса", font=("Arial", 14, "bold"))

# дерево
def tree(x, y, size, colorTrunk, colorLeaves):
    trunkWidth = size/3
    trunkHeight = size
    leaves1Radius = size/1.5
    leaves2Radius = leaves1Radius/1.5
    leaves3Radius = leaves2Radius/1.5

    # рисуем ствол
    prepare(x, y, colorTrunk, 7)
    pen.begin_fill()
    pen.setheading(90)
    pen.forward(trunkHeight)
    pen.right(90)
    pen.forward(trunkWidth)
    pen.right(90)
    pen.forward(trunkHeight)
    pen.right(90)
    pen.forward(trunkWidth)
    pen.end_fill()

    # рисуем листья нижние
    circleX = x + trunkWidth/2
    circleY = y + trunkHeight - trunkHeight/4
    prepare(circleX, circleY, colorLeaves, 7)
    pen.begin_fill()
    pen.circle(leaves1Radius)
    pen.end_fill()

    # рисуем листья средние
    circleY = circleY + leaves1Radius + leaves1Radius/2
    prepare(circleX, circleY, colorLeaves, 7)
    pen.begin_fill()
    pen.circle(leaves2Radius)
    pen.end_fill()





# начинаем рисовать тут
house(100, 0, 150, "red", "green")
house(200, 40, 100, "yellow", "green")
fox(-300, -200, "orange")
fox(0, -200, "brown")
tree(-100, 0, 50, "brown", "green")
tree(-200, 0, 50, "brown", "green")
tree(-300, 0, 90, "brown", "green")
tree(-50, 0, 60, "brown", "green")
tree(0, 0, 80, "brown", "green")












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
