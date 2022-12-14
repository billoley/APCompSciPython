# import modules
from tkinter import *

# initialize variables
total_price = 0


# define functions
def gpbj_selected():
    global total_price
    GPBJ_PRICE = 3.75
    total_price += GPBJ_PRICE
    current_total_lbl.config(text="$%.2f" % total_price)


def spbj_selected():
    global total_price
    SPBJ_PRICE = 4.25
    total_price += SPBJ_PRICE
    current_total_lbl.config(text="$%.2f" % total_price)


def ccc_selected():
    global total_price
    CCC_PRICE = 1.89
    total_price += CCC_PRICE
    current_total_lbl.config(text="$%.2f" % total_price)


def coffee_selected():
    global total_price
    COFFEE_PRICE = 0.99
    total_price += COFFEE_PRICE
    current_total_lbl.config(text="$%.2f" % total_price)


def order_completed():
    global total_price
    total_price *= 1.06  # 6% tax
    final_total_lbl.config(text="Your total today is $%.2f." % total_price)


def reset_order():
    global total_price
    total_price = 0
    current_total_lbl.config(text="$%.2f" % total_price)
    final_total_lbl.config(text="")


# main window setup
root = Tk()  # create main window
root.title("DANZA PBJ - Order Screen")  # set title of window
root.geometry("320x200")  # set size of window

# creating buttons
grape_pbj_btn = Button(root, text="Grape PBJ", command=gpbj_selected, bg="purple", fg="white")
strawberry_pbj_btn = Button(root, text="Strawberry PBJ", command=spbj_selected, bg="red", fg="white")
chocchip_cookie_btn = Button(root, text="Choc Chip Cookie", command=ccc_selected, bg="black", fg="white")
coffee_btn = Button(root, text="Coffee", command=coffee_selected, bg="brown", fg="white")
order_complete_btn = Button(root, text="Complete", command=order_completed, bg="green", fg="white")
reset_btn = Button(root, text="Reset", command=reset_order)

# creating labels
current_total_lbl = Label(root, text="$0.00")
final_total_lbl = Label(root)

# adding widgets to main window (buttons, labels, etc.)
current_total_lbl.pack()
grape_pbj_btn.pack()
strawberry_pbj_btn.pack()
chocchip_cookie_btn.pack()
coffee_btn.pack()
order_complete_btn.pack()
final_total_lbl.pack()
reset_btn.pack()

# keep window up and running
root.mainloop()
