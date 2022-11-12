import time
import sys
import random

print("DRAGON ADVENTURE")
time.sleep(1)
print("Created by Mr. Danza\n")
time.sleep(2)
print("Welcome to Arwaltz. My name is Harry.")
time.sleep(1)
player_name = input("What's your name?\n")
print("Shhhh...not so loud " + player_name + "!")
time.sleep(1)
print("They may hear you.")
time.sleep(1)
print("Let's go to a safe place.")
time.sleep(1)
print("There are some things I need to tell you about.")
time.sleep(3)
print("Okay...we're good now.")
time.sleep(2)
print("Up ahead there are several caves.")
time.sleep(2)
print("In each cave there is treasure!")
time.sleep(2)
print("But dragons also live inside of caves.")
time.sleep(2)
print("So we have to be very careful!")
time.sleep(2)
print("Many of my friends have been eaten by dragons...")
time.sleep(3)

while True:
    play_game = input("Will you help me?\n")
    play_game = play_game.lower()
    if play_game == "yes":
        print("Okay! Let's do this!")
        time.sleep(3)
        break
    elif play_game == "no":
        print("Well then get out of here, before it's too late!")
        print(player_name + " ran away scared.")
        sys.exit()
    else:
        print("I don't understand.")
        continue

gold = 10
tunnels = ["left", "right"]

while True:
    print("I see a cave!")
    time.sleep(2)
    go_in = input("Should we go in?\n")
    if go_in == "yes":
        print("There are two tunnels.")
        time.sleep(2)
        print("One will lead to a hungry dragon")
        time.sleep(2)
        print("The other will lead us to treasure!")
        time.sleep(2)
        direction = input("Should we go right or left?\n")
        bad_tunnel = random.choice(tunnels)
        if direction != "right" and direction != "left":
            print("I can't understand you.")
            time.sleep(2)
            print("Let's go to a different cave.")
            time.sleep(2)
            continue
        elif direction == bad_tunnel:
            time.sleep(2)
            print("Oh no! There's a dragon in this tunnel.")
            time.sleep(2)
            payment = random.randint(1, 10)
            print("The dragon wants " + str(payment) + " gold coins")
            time.sleep(2)
            print("We have " + str(gold) + " gold")
            gold -= payment
            time.sleep(2)
            print("***PAYS DRAGON***")
            time.sleep(2)
            print("We now have " + str(gold) + " gold coins")
            time.sleep(2)
            print("Hurry, let's get out of here and look for another cave.")
            time.sleep(2)
            if gold < 0:
                print("We don't have enough gold!")
                time.sleep(2)
                print("Oh no!!")
                time.sleep(2)
                print(player_name + " was eaten by the dragon")
                sys.exit()
        else:
            time.sleep(2)
            print("There's treasure in this tunnel!")
            time.sleep(2)
            coins = random.randint(1, 10)
            print("There are " + str(coins) + " gold coins!")
            time.sleep(2)
            gold += coins
            print("We now have " + str(gold) + " gold coins.")
            time.sleep(2)
            print("Let's keep going!")
            time.sleep(2)
            continue
    else:
        go_home = input("Should we go home?\n")
        if go_home == "yes":
            print("Okay let's leave.")
            time.sleep(2)
            print("***LEAVES WITH " + str(gold) + " GOLD COINS***")
            sys.exit()
        else:
            print("Let's just look for another cave.")
            time.sleep(2)
            continue
