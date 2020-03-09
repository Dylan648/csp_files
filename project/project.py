import turtle, tkinter as tk

screen = turtle.Screen()
jump = False


def handle_jump():
    dino.forward(200)
    dino.back(200)

sprite = 'sprites/dino.gif'
screen.addshape(sprite)
# obs = 'sprites/log.gif'
# screen.addshape(obs)
dino = turtle.Turtle(sprite)

ground = turtle.Turtle()
ground.hideturtle()

obstacle = turtle.Turtle()
ground.speed(0)
dino.shapesize(1)
dino.penup()
dino.goto(-150, 0)
dino.left(90)

ground.penup()
ground.goto(-600,-100)
ground.pendown()
ground.forward(1000)

obstacle.penup()
obstacle.goto(300,0)

screen.onkeypress(handle_jump, 'space')

while obstacle.xcor() != dino.xcor():
    obstacle.back(10)

screen.listen()
screen.mainloop()