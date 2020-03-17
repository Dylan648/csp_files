import turtle, tkinter as tk, random
import gdx

gdx = gdx.gdx()
screen = turtle.Screen()
game_over = False
jump = False
score = 0
game_over = False

gdx.open_usb()
gdx.select_sensors([1])
gdx.start(period=100)

def handle_jump():
    global jump
    measure = gdx.read()
    if not jump and measure[-1] >= 70:
        jump = True
        dino_dy = -8
        animate()

def move_enemy():
    if jump:
        obstacle.back(20)
    else:
        obstacle.back(10)
    if not game_over:
        screen.ontimer(move_enemy, 5)
    else:
        obstacle.back(5)

def animate():
    global dino_dy
    global junp
    dino.up(dino_dy)
    dino_dy += gravity
    if dino.ycor() > 250:
        dino_dy = 0
        dino.goto(-150, -75)
        jump = False
    if jump:
        screen.ontimer(animate, 10)
        


def respawn_enemy():
    if obstacle.xcor() == -500:
        obstacle.hideturtle()
        obstacle.goto(300,-75)
        obstacle.showturtle()
    screen.ontimer(respawn_enemy, 5)

def count_change():
    global score
    global game_over
    if not game_over:
        if obstacle.xcor() == dino.xcor() - 10:
            score += 1
            counter.goto(0,250)
            counter.setheading(0)
            counter.clear()
            counter.write(score, align='right', font=('Ariel', 20, 'normal'))
        screen.ontimer(count_change, 25)

def check_collision():
    global score
    global game_over
    if dino.ycor() == obstacle.ycor() and dino.xcor() == obstacle.xcor():
        game_over = True
        score = 0
        counter.goto(0,250)
        counter.setheading(0)
        counter.clear()
        counter.write(score, align='right', font=('Ariel', 20, 'normal'))
        restarter.penup()
        restarter.goto(0, 100)
        restarter.setheading(0)
        restarter.write('GAME OVER, Press r to restart the game', align='center', font=('Ariel', 30, 'normal'))
    screen.ontimer(check_collision, 15)

def restart():
    global game_over
    if game_over:
        game_over = False
        restarter.clear()
        start_game()

def start_game():
    handle_jump()
    move_enemy()
    respawn_enemy()
    check_collision()
    count_change()
    screen.onkeypress(restart, 'r')
    obstacle.penup()
    obstacle.hideturtle()
    obstacle.goto(300,-75)
    obstacle.showturtle()

    screen.listen()
    screen.mainloop()

sprite = 'sprites/dino.gif'
screen.addshape(sprite)
# obs = 'sprites/log.gif'
# screen.addshape(obs)
dino = turtle.Turtle(sprite)

ground = turtle.Turtle()
ground.hideturtle()
stationary_score = turtle.Turtle()
stationary_score.hideturtle()
counter = turtle.Turtle()
counter.hideturtle()
restarter = turtle.Turtle()
restarter.hideturtle()
obstacle = turtle.Turtle()
obstacle.shape('turtle')
obstacle.hideturtle()
ground.speed(0)
dino.shapesize(1)
dino.penup()
dino.speed(4)
dino.goto(-150, -75)
dino.left(90)
dino_dy = 0
gravity = .2

ground.penup()
ground.goto(-600,-100)
ground.pendown()
ground.forward(1000)

counter.penup()
stationary_score.penup()
stationary_score.goto(-100, 250)
stationary_score.setheading(0)
stationary_score.write('Score = ', align='left', font=('Ariel', 20, 'normal'))


obstacle.penup()
obstacle.goto(300,-75)
obstacle.showturtle()

start_game()