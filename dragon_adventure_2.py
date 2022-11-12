# -------------------------DRAGON ADVENTURE 2----------------------------- #
# I created Dragon Adventure with my AP students earlier in the year as a  #
# choose your own adventure game using input functions. This is an upgrade #
# using the Turtle and Tkinter modules.                                    #
# ------------------------------------------------------------------------ #

# import modules
import turtle
import math
import random
import time
from tkinter import *

# screen
wn = turtle.Screen()
wn.title("Dragon Adventure 2")
wn.bgcolor("red")

# border
border = turtle.Turtle()
border.pencolor("black")
border.speed(0)
border.penup()
border.setposition(-200, 200)
border.pendown()
border.pensize(5)
for side in range(4):
    border.forward(400)
    border.right(90)
border.hideturtle()
border.write("Dragon Adventure 2 - Coins: 10", False, align="left", font=("Arial", 14, "normal"))

# player
player = turtle.Turtle()
player.color("white")
player.penup()
player.speed(0)

# cave
cave = turtle.Turtle()
cave.shape("circle")
cave.penup()
cave.speed(0)
cave.setposition(random.randint(-200, 200), random.randint(-200, 200))

# variables and lists
speed = 1
score = 0
tunnels = ["right", "left"]
coins = 10


# functions
def turn_left():
    player.left(25)


def turn_right():
    player.right(25)


def collide(a, b):
    c = math.sqrt(math.pow(a.xcor() - b.xcor(), 2) + math.pow(a.ycor() - b.ycor(), 2))
    if c < 20:
        return True
    else:
        return False


def random_dragon():
    global dragon_tunnel
    dragon_tunnel = random.choice(tunnels)


def left_tun_select():
    global tunnel_choice
    tunnel_choice = "left"
    result()


def right_tun_select():
    global tunnel_choice
    tunnel_choice = "right"
    result()


def quit_game():
    turtle.bye()
    root.destroy()


def result():
    global coins
    global root2
    rand_coins_amt = random.randint(1, 10)
    random_dragon()
    root.destroy()

    # post-choice alert tkinter window
    root2 = Tk()
    root2.title("!!!")

    result1_lbl = Label(root2)
    result2_lbl = Label(root2)
    resume_btn = Button(root2, text="Resume Game", command=resume)
    result1_lbl.pack()
    result2_lbl.pack()
    resume_btn.pack()

    if tunnel_choice == dragon_tunnel:
        result1_lbl.config(text=f"A dragon appears and demands {rand_coins_amt} coins.")
        coins -= rand_coins_amt
        if coins < 0:
            result2_lbl.config(text="You don't have enough coins! The dragon eats you. Game over!")
            resume_btn.pack_forget()
        else:
            result2_lbl.config(text=f"You now have {coins} coins remaining.")

    else:
        result1_lbl.config(text=f"You found {rand_coins_amt} coins!")
        coins += rand_coins_amt
        result2_lbl.config(text=f"You now have {coins} coins.")

    # update score in turtle window
    border.undo()
    border.penup()
    border.hideturtle()
    border.setposition(-200, 200)
    score_string = "Dragon Adventure 2 - Coins: %s" % coins
    border.write(score_string, False, align="left", font=("Arial", 14, "normal"))


def resume():
    global speed
    speed = 1
    root2.destroy()


# bindings
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")

# gameplay in turtle window
while True:
    player.forward(speed)
    # boundary and collision checks
    if player.xcor() > 200 or player.xcor() < -200:
        player.right(180)
    if player.ycor() > 200 or player.ycor() < -200:
        player.right(180)
    if collide(player, cave):
        cave.setposition(random.randint(-200, 200), random.randint(-200, 200))
        index = random.randint(0, 2)
        speed = 0

        # choose tunnel tkinter window
        root = Tk()
        root.geometry("220x175")
        root.title("Choose A Tunnel")

        story1_lbl = Label(root, text="You enter the cave and see two tunnels")
        story2_lbl = Label(root, text="One of the tunnels leads to treasure")
        story3_lbl = Label(root, text="The other leads to a hungry dragon")
        story4_lbl = Label(root, text="Choose a tunnel")
        story5_lbl = Label(root)

        go_left_btn = Button(root, text="Left", command=left_tun_select)
        go_right_btn = Button(root, text="Right", command=right_tun_select)
        quit_btn = Button(root, text="Quit", command=quit_game)

        story1_lbl.grid(row=0, columnspan=2)
        story2_lbl.grid(row=1, columnspan=2)
        story3_lbl.grid(row=2, columnspan=2)
        story4_lbl.grid(row=3, columnspan=2)
        story5_lbl.grid(row=4, columnspan=2)
        go_left_btn.grid(row=5, column=0)
        go_right_btn.grid(row=5, column=1)
        quit_btn.grid(row=6, columnspan=2)

wn.mainloop()
