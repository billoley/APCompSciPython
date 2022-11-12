import random
from tkinter import *

root = Tk()

choices = ("Rock", "Paper", "Scissors")
stats = {"wins": 0, "losses": 0, "ties": 0}


def throw(your_throw):
    cpu_throw = random.choice(choices)
    check_winner(cpu_throw, your_throw)


def check_winner(cpu, player):
    global stats
    if (player == "Rock" and cpu == "Scissors") or \
            (player == "Scissors" and cpu == "Paper") or \
            (player == "Paper" and cpu == "Rock"):
        stats["wins"] += 1
        result_lbl.configure(text=f"You win! {player} beats {cpu}.")
        stats_update()
    elif player == cpu:
        stats["ties"] += 1
        result_lbl.configure(text=f"Tie! {player} ties {cpu}.")
        stats_update()
    else:
        stats["losses"] += 1
        result_lbl.configure(text=f"You lose! {cpu} beats {player}.")
        stats_update()


def stats_update():
    stats_lbl.configure(text=f"Wins: {stats['wins']} \
    Losses: {stats['losses']} Ties: {stats['ties']}")


rock_btn = Button(root, text="Rock", command=lambda: throw(choices[0]))
paper_btn = Button(root, text="Paper", command=lambda: throw(choices[1]))
scissors_btn = Button(root, text="Scissors", command=lambda: throw(choices[2]))
result_lbl = Label(root, text="Shoot!")
stats_lbl = Label(root, text=f"Wins: {stats['wins']} Losses: {stats['losses']} Ties: {stats['ties']}")

result_lbl.grid(row=0, columnspan=3)
rock_btn.grid(row=1, column=0)
paper_btn.grid(row=1, column=1)
scissors_btn.grid(row=1, column=2)
stats_lbl.grid(row=2, columnspan=3)

root.mainloop()
