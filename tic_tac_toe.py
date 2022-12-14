# c0  c1  c2
# -----------#
# 0 | 1 | 2 # r0
# -----------#
# 3 | 4 | 5 # r1
# -----------#
# 6 | 7 | 8 # r2
# -----------#

# winners 012, 345, 678, 036, 147, 258, 048, 246

from tkinter import *

x_or_o = "X"
color = "red"
hidden_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def change_xo():  # take turns between x's and o's
    global x_or_o
    if x_or_o == "X":
        x_or_o = "O"
    else:
        x_or_o = "X"


def change_color():  # switch between the red and yellow colors
    global color
    if color == "red":
        color = "yellow"
    else:
        color = "red"


def check_winner():
    if (hidden_board[0] == x_or_o and hidden_board[1] == x_or_o and hidden_board[2] == x_or_o) or \
            (hidden_board[3] == x_or_o and hidden_board[4] == x_or_o and hidden_board[5] == x_or_o) or \
            (hidden_board[6] == x_or_o and hidden_board[7] == x_or_o and hidden_board[8] == x_or_o) or \
            (hidden_board[0] == x_or_o and hidden_board[3] == x_or_o and hidden_board[6] == x_or_o) or \
            (hidden_board[1] == x_or_o and hidden_board[4] == x_or_o and hidden_board[7] == x_or_o) or \
            (hidden_board[2] == x_or_o and hidden_board[5] == x_or_o and hidden_board[8] == x_or_o) or \
            (hidden_board[0] == x_or_o and hidden_board[4] == x_or_o and hidden_board[8] == x_or_o) or \
            (hidden_board[2] == x_or_o and hidden_board[4] == x_or_o and hidden_board[6] == x_or_o):
        result_label.configure(text=f"{x_or_o}'s has won the game!")
        for i in buttons:
            i.configure(state=DISABLED)


def check_tie():
    if 0 not in hidden_board:
        result_label.configure(text="Tie!")


def btn_selected(num):  # whenever a button is clicked, do this
    global x_or_o
    global color
    buttons[num].configure(text=x_or_o, bg=color, state=DISABLED)
    hidden_board[num] = x_or_o
    check_winner()
    check_tie()
    change_xo()
    change_color()


root = Tk()
root.title("Tic-Tac-Toe")

button0 = Button(root, height=2, width=5, command=lambda: btn_selected(0))
button1 = Button(root, height=2, width=5, command=lambda: btn_selected(1))
button2 = Button(root, height=2, width=5, command=lambda: btn_selected(2))
button3 = Button(root, height=2, width=5, command=lambda: btn_selected(3))
button4 = Button(root, height=2, width=5, command=lambda: btn_selected(4))
button5 = Button(root, height=2, width=5, command=lambda: btn_selected(5))
button6 = Button(root, height=2, width=5, command=lambda: btn_selected(6))
button7 = Button(root, height=2, width=5, command=lambda: btn_selected(7))
button8 = Button(root, height=2, width=5, command=lambda: btn_selected(8))
result_label = Label(root)

buttons = [button0, button1, button2, button3, button4, button5, button6, button7, button8]

button0.grid(row=0, column=0)
button1.grid(row=0, column=1)
button2.grid(row=0, column=2)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)
button5.grid(row=1, column=2)
button6.grid(row=2, column=0)
button7.grid(row=2, column=1)
button8.grid(row=2, column=2)
result_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
