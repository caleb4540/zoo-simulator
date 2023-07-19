import turtle
import time
import random

snake_hab_money = 100
panda_hab_money = 100
elephant_hab_money = 100
needed_for_snake = 100
needed_for_panda = 100
needed_for_elephant = 100
coins1 = 100
habitats = 0
times = 0
bob = 5

screen = turtle.Screen()
screen.title("zoo simulator")
screen.bgcolor("White")

turtle.register_shape("elephant habitat.gif")
turtle.register_shape("snake habitat.gif")
turtle.register_shape("panda habitat.gif")
turtle.register_shape("elephant.gif")
turtle.register_shape("snake.gif")
turtle.register_shape("panda.gif")
turtle.register_shape("snakey.gif")

snakey = turtle.Turtle()
snakey.penup()
snakey.shape("snakey.gif")
snakey.goto(300, 250)
snakeyx = 300

line = turtle.Turtle()
line.penup()
line.color("black")
line.shape("square")
line.goto(0, -200)
line.shapesize(0.2, 50, 0.2)

coins = turtle.Turtle()
coins.hideturtle()
coins.penup()
coins.goto(-300, 300)
coins.write("coins:" + str(coins1), font=("arial", 16, "normal"))

panda_button = turtle.Turtle()
panda_button.penup()
panda_button.shape("panda habitat.gif")
panda_button.goto(-70, -265)
p_writer = turtle.Turtle()
p_writer.hideturtle()
p_writer.penup()
p_writer.goto(-70, -250)
p_writer.write("" + str(needed_for_panda), font=("arial", 16, "bold"))
pa_writer = turtle.Turtle()
pa_writer.hideturtle()
pa_writer.penup()
pa_writer.goto(200, 100)
pa_writer.write("" + str(panda_hab_money), font=("arial", 16, "bold"))

snake_button = turtle.Turtle()
snake_button.penup()
snake_button.shape("snake habitat.gif")
snake_button.goto(-190, -265)
s_writer = turtle.Turtle()
s_writer.hideturtle()
s_writer.penup()
s_writer.goto(-190, -250)
s_writer.write("" + str(needed_for_snake), font=("arial", 16, "bold"))
sn_writer = turtle.Turtle()
sn_writer.hideturtle()
sn_writer.penup()
sn_writer.goto(0, 100)
sn_writer.write("" + str(snake_hab_money), font=("arial", 16, "bold"))

elephant_button = turtle.Turtle()
elephant_button.penup()
elephant_button.shape("elephant habitat.gif")
elephant_button.goto(-310, -265)
e_writer = turtle.Turtle()
e_writer.hideturtle()
e_writer.penup()
e_writer.goto(-310, -250)
e_writer.write("" + str(needed_for_elephant), font=("arial", 16, "bold"))
el_writer = turtle.Turtle()
el_writer.hideturtle()
el_writer.penup()
el_writer.goto(-200, 100)
el_writer.write("" + str(elephant_hab_money), font=("arial", 16, "bold"))

elephant_hab = turtle.Turtle()
elephant_hab.penup()
elephant_hab.goto(-200, 0)
elephant_hab.shape("elephant.gif")

snake_hab = turtle.Turtle()
snake_hab.penup()
snake_hab.goto(0, 0)
snake_hab.shape("snake.gif")

panda_hab = turtle.Turtle()
panda_hab.penup()
panda_hab.goto(200, 0)
panda_hab.shape("panda.gif")

def snake(x, y):
    global snake_hab_money, needed_for_snake, coins1
    if coins1 >= needed_for_snake:
        coins1 = coins1 - needed_for_snake
        snake_hab_money = snake_hab_money * 2
        needed_for_snake = needed_for_snake * 3
        coins.clear()
        coins.write("coins:" + str(coins1), font=("arial", 16, "normal"))
        s_writer.clear()
        s_writer.write("" + str(needed_for_snake), font=("arial", 16, "bold"))
        sn_writer.clear()
        sn_writer.write("" + str(snake_hab_money), font=("arial", 16, "bold"))

def panda(x, y):
    global panda_hab_money, needed_for_panda, coins1
    if coins1 >= needed_for_panda:
        coins1 = coins1 - needed_for_panda
        panda_hab_money = panda_hab_money * 2
        needed_for_panda *= 3
        coins.clear()
        coins.write("coins:" + str(coins1), font=("arial", 16, "normal"))
        p_writer.clear()
        p_writer.write("" + str(needed_for_panda), font=("arial", 16, "bold"))
        pa_writer.clear()
        pa_writer.write("" + str(panda_hab_money), font=("arial", 16, "bold"))

def elephant(x, y):
    global elephant_hab_money, needed_for_elephant, coins1
    if coins1 >= needed_for_elephant:
        coins1 = coins1 - needed_for_elephant
        elephant_hab_money = elephant_hab_money * 2
        needed_for_elephant = needed_for_elephant * 3
        coins.clear()
        coins.write("coins:" + str(coins1), font=("arial", 16, "normal"))
        e_writer.clear()
        e_writer.write("" + str(needed_for_elephant), font=("arial", 16, "bold"))
        el_writer.clear()
        el_writer.write("" + str(elephant_hab_money), font=("arial", 16, "bold"))

def collect():
    global coins1, elephant_hab_money, panda_hab_money, snake_hab_money
    coins1 = coins1 + elephant_hab_money + snake_hab_money + panda_hab_money
    coins.clear()
    coins.write("coins:" + str(coins1), font=("arial", 16, "normal"))
    screen.ontimer(collect , 5000)

def hi():
    global snakeyx, times
    if snakeyx == -290:
        snakeyx = 300
    snakeyx = snakeyx - 5
    snakey.goto(snakeyx, 250)

def move_snakey():
    global snakeyx
    if snakeyx <= -310:
        snakey.hideturtle()
        snakeyx = 310
    snakeyx -= 5
    snakey.goto(snakeyx, 250)
    snakey.showturtle()
    turtle.ontimer(move_snakey, 50)

turtle.listen()
elephant_button.onclick(elephant)
panda_button.onclick(panda)
snake_button.onclick(snake)

turtle.ontimer(collect, 5000)
turtle.ontimer(move_snakey, 50)

turtle.mainloop()








