import random
import time

# initialize lists and variables
possible_guesses = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
five_letter_words = ["field", "glove", "stick", "plate", "score"]
money_values = [0, 200, 250, 300, 350, 400, 450, 500, 600, 700, 1000, 5000]
correct_letter_guesses = []
incorrect_letter_guesses = []
puzzle_board = "_____"
num_incorrect_guesses = 0
total_prize_money = 0


# functions
def rules():
    print("Rules Of The Game:")
    time.sleep(2)
    print("You will be given a random blank puzzle to start.")
    time.sleep(2)
    print("The puzzle will be a five letter word.")
    time.sleep(2)
    print("The wheel will automatically spin for you,")
    time.sleep(2)
    print("and the spinner will land on a random prize amount.")
    time.sleep(2)
    print("You must guess a lower-case letter (no numbers or symbols).")
    time.sleep(2)
    print("If you guess a correct letter in the puzzle, it will show up on the board.")
    time.sleep(2)
    print("After 5 incorrect letter guesses, you lose the game.")
    time.sleep(2)
    print("Lists of your correct and incorrect letter guesses will be provided.")
    time.sleep(2)


#########game starts here#########

# game title
print("W H E E L    O F    F O R T U N E")
time.sleep(3)

# game rules
rules()

# select a random word from list
print("The category is 'Sports'.")
secret_word = random.choice(five_letter_words)

# the board
print(f"Puzzle Board: {puzzle_board}")
time.sleep(2)

while True:
    # the spin
    print(f"Total Prize Money: ${total_prize_money}")
    print("You spin the wheel and land on...")
    time.sleep(3)
    spin_value = random.choice(money_values)
    if spin_value == 0:
        print("Bankrupt!")
        total_prize_money = 0
        print("You just lost all your money.")
        num_incorrect_guesses += 1
        continue
    else:
        print(f"${spin_value}")
    time.sleep(2)

    # letter guess update
    print(f"Correct Guesses: {correct_letter_guesses}")
    print(f"Incorrect Guesses: {incorrect_letter_guesses}")
    time.sleep(2)

    # the letter guess
    letter_guess = input("Guess a letter. ")
    if letter_guess in possible_guesses:
        if letter_guess in secret_word:
            # correct letter guess
            for i in range(5):
                if secret_word[i] == letter_guess:
                    puzzle_board = puzzle_board[:i] + letter_guess + puzzle_board[i + 1:]
            print("*DING* Correct guess!")
            time.sleep(2)
            print(f"Puzzle Board: {puzzle_board}")
            time.sleep(2)
            total_prize_money += spin_value
            correct_letter_guesses.append(letter_guess)
            if "_" not in puzzle_board:
                print("You have solved the puzzle")
                time.sleep(2)
                print(f"You win ${total_prize_money}")
                break
        else:
            # incorrect letter guess
            print("*BUZZER SOUNDS* Incorrect guess!")
            print(f"Puzzle Board: {puzzle_board}")
            incorrect_letter_guesses.append(letter_guess)
            num_incorrect_guesses += 1
            if num_incorrect_guesses == 5:
                print("You have exceeded the number of incorrect guesses")
                time.sleep(2)
                print(f"The word was '{secret_word}'.")
                time.sleep(2)
                print("GAME OVER!")
                break

    else:
        print("Please guess a lower-case letter. Let's respin the wheel.")
        time.sleep(2)
