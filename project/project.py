import turtle, tkinter as tk

screen = turtle.Screen()
game_over = False
jump = False
score = 0

def handle_jump():
    dino.forward(220)
    dino.back(220)
    jump = True

def move_enemy():
    if jump:
        obstacle.back(20)
    else:
        obstacle.back(10)
    if not game_over:
        screen.ontimer(move_enemy, 5)

def respawn_enemy():
    if obstacle.xcor() == -500:
        obstacle.hideturtle()
        obstacle.goto(300,0)
        obstacle.showturtle()
    screen.ontimer(respawn_enemy, 5)

sprite = 'sprites/dino.gif'
screen.addshape(sprite)
# obs = 'sprites/log.gif'
# screen.addshape(obs)
dino = turtle.Turtle(sprite)

ground = turtle.Turtle()
ground.hideturtle()
counter = turtle.Turtle()
counter.hideturtle()
obstacle = turtle.Turtle()
obstacle.shape('turtle')
ground.speed(0)
dino.shapesize(1)
dino.penup()
dino.speed(4)
dino.goto(-150, 0)
dino.left(90)

ground.penup()
ground.goto(-600,-100)
ground.pendown()
ground.forward(1000)

counter.penup()
counter.left(90)
counter.forward(250)
counter.right(90)
counter.write('Score = ', align='left', font=('Ariel', 20, 'normal'))
counter.forward(100)
counter.write(score, align='right', font=('Ariel', 20, 'normal'))
obstacle.penup()
obstacle.goto(300,0)

screen.onkeypress(handle_jump, 'space')
move_enemy()
respawn_enemy()

screen.listen()
screen.mainloop()