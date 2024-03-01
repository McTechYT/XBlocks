import turtle
from functions import *

turtle.hideturtle()
turtle.speed(90000)
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown() 

turtle.listen()

generateTerrain()
turtle.goto(-200, -150)

turtle.onkey(drawGrass, "g")

turtle.onkey(drawDirt, "d")

turtle.onkey(drawCobble, "c")

turtle.onkey(delete, "q")

turtle.onkey(water, "w")

turtle.onkey(leaves, "l")

turtle.onkey(planks, "p")

turtle.onkey(moveright, "Right")

turtle.onkey(moveleft, "Left")

turtle.onkey(moveup, "Up")

turtle.onkey(movedown, "Down")

turtle.exitonclick()
