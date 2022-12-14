# RPS

# IDEAS
# list to track last 10 - record, cputhrows, userthrows, record with rock, record with scissors, record with paper, record vs. each, number of throws of each kind - user and cpu, combined stats

# imports
import random

attacks = ["rock", "paper", "scissors"]

# initialize score variables
wins = 0
losses = 0
ties = 0

while True:
    cpu_throw = random.choice(attacks)
    user_throw = input("Rock, Paper, or Scissors?\n")
    user_throw = user_throw.lower()

    if user_throw == "q":
        break
    elif user_throw not in attacks:
        print("Please try again.")
        continue

    print("You chose " + user_throw)
    print("CPU chose " + cpu_throw)

    if (user_throw == "rock" and cpu_throw == "scissors") or (user_throw == "paper" and cpu_throw == "rock") or (
            user_throw == "scissors" and cpu_throw == "paper"):
        print("You win!")
        wins += 1
    elif (user_throw == "rock" and cpu_throw == "paper") or (user_throw == "paper" and cpu_throw == "scissors") or (
            user_throw == "scissors" and cpu_throw == "rock"):
        print("You lose!")
        losses += 1
    else:
        print("Tie!")
        ties += 1

    plays = wins + losses + ties
    wp = wins / plays  # winning percentage
    prp = (wins + ties) / plays  # positive result percentage
    pts = (wins * 3) + (ties * 1)
    ppp = pts / plays  # points per play
    zscore = wins - losses
    zplays = wins + losses
    if zplays == 0:
        zquality = 0
    else:
        zquality = (wins / zplays) * 100

    print(str(wins) + "-" + str(losses) + "-" + str(ties))
    print("| W | L | T | l | W%  | PRP | Pts | PPP | Zs | Zp | Zq | ")
    print("------------------------------------------------------")
    print("|", wins, "|", losses, "|", ties, "|", plays, "|", round(wp, 3), "|", round(prp, 3), "|", pts, "|",
          round(ppp, 3), "|", zscore, "|", zplays, "|", round(zquality), "|")
    print("------------------------------------------------------")
