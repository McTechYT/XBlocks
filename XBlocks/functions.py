import turtle

def generateTerrain():
  for i in range(10):
    drawGrass()
  movedown2(500)

  for i in range(2):
    for i in range(10):
      drawDirt()
    movedown2(500)

  for i in range(2):
    for i in range(10):
      drawCobble()
    movedown2(500)


def newBlock():
  turtle.penup()
  turtle.move()

def movedown2(size):
  turtle.penup()
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(size)
  turtle.left(180)

def moveright():
  turtle.showturtle()
  turtle.forward(50)

def moveleft():
  turtle.showturtle()
  turtle.backward(50)

def movedown():
  turtle.showturtle()
  turtle.right(90)
  turtle.forward(50)
  turtle.left(90)

def moveup():
  turtle.showturtle()
  turtle.left(90)
  turtle.forward(50)
  turtle.right(90)

def drawGrass():
  turtle.hideturtle()
  turtle.pendown()
  turtle.fillcolor("brown")
  turtle.begin_fill()
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.end_fill()
  #
  turtle.color("green")
  turtle.penup()
  turtle.right(180)
  turtle.forward(10)
  turtle.left(90)
  turtle.pendown()
  turtle.fillcolor("green")
  turtle.begin_fill()
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(10)
  turtle.end_fill()
  #
  turtle.penup()
  turtle.right(180)
  turtle.forward(10)
  turtle.right(90)
  turtle.forward(50)


def drawCobble():
  turtle.hideturtle()
  turtle.pendown()
  turtle.color("gray")
  turtle.fillcolor("gray")
  turtle.begin_fill()
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.end_fill()
  #
  turtle.penup()
  turtle.right(90)
  turtle.forward(50)


def drawDirt():
  turtle.hideturtle
  turtle.pendown()
  turtle.color("brown")
  turtle.fillcolor("brown")
  turtle.begin_fill()
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.end_fill()
  #
  turtle.penup()
  turtle.right(90)
  turtle.forward(50)

def delete():
  turtle.hideturtle()
  turtle.pendown()
  turtle.color("white")
  turtle.fillcolor("white")
  turtle.begin_fill()
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.end_fill()
  #
  turtle.penup()
  turtle.right(90)
  turtle.forward(50)
  turtle.color("black")

def water():
  turtle.hideturtle()
  turtle.pendown()
  turtle.color("blue")
  turtle.fillcolor("blue")
  turtle.begin_fill()
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.end_fill()
  #
  turtle.penup()
  turtle.right(90)
  turtle.forward(50)

def leaves():
  turtle.hideturtle()
  turtle.pendown()
  turtle.color("green")
  turtle.fillcolor("green")
  turtle.begin_fill()
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.end_fill()
  #
  turtle.penup()
  turtle.right(90)
  turtle.forward(50)

def planks():
  turtle.hideturtle()
  turtle.pendown()
  turtle.color("burlywood4")
  turtle.fillcolor("burlywood4")
  turtle.begin_fill()
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)
  turtle.forward(50)
  turtle.end_fill()
  #
  turtle.penup()
  turtle.right(90)
  turtle.forward(50)