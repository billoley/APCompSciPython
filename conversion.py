# ___ ___ ___ ___ ___ ___ ___ ___
# 128 64  32  16  8   4   2   1

from tkinter import *

nums = []
dec1 = 0
dec2 = 0
bin2 = ""
eight = [128, 64, 32, 16, 8, 4, 2, 1]


def compile_num():
    for i in binary_entries:
        n = int(i.get())
        nums.append(n)


def calc_decimal():
    global dec1
    global nums
    exp = 7
    ind = 0
    compile_num()
    for i in nums:
        dec1 += (nums[ind] * (2 ** exp))
        exp -= 1
        ind += 1
    dec_lbl.configure(text=dec1)
    nums = []
    dec1 = 0


def calc_binary():
    global bin2
    dec2 = int(dec_entry.get())
    for i in eight:
        if dec2 >= i:
            bin2 = bin2 + "1"
            dec2 -= i
        else:
            bin2 = bin2 + "0"
    bin_lbl.configure(text=bin2)
    dec2 = 0
    bin2 = ""


root = Tk()

bindec_lbl = Label(root, text="Binary -> Decimal")
entry1 = Entry(root, width=3)
entry2 = Entry(root, width=3)
entry3 = Entry(root, width=3)
entry4 = Entry(root, width=3)
entry5 = Entry(root, width=3)
entry6 = Entry(root, width=3)
entry7 = Entry(root, width=3)
entry8 = Entry(root, width=3)
convdec_btn = Button(root, text="CONVERT", command=calc_decimal)
dec_lbl = Label(root)
spacer_lbl = Label(root)

binary_entries = [entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8]

decbin_lbl = Label(root, text="Decimal -> Binary")
dec_entry = Entry(root)
convbin_btn = Button(root, text="CONVERT", command=calc_binary)
bin_lbl = Label(root)

bindec_lbl.grid(row=0, columnspan=8)
entry1.grid(row=1, column=0)
entry2.grid(row=1, column=1)
entry3.grid(row=1, column=2)
entry4.grid(row=1, column=3)
entry5.grid(row=1, column=4)
entry6.grid(row=1, column=5)
entry7.grid(row=1, column=6)
entry8.grid(row=1, column=7)
convdec_btn.grid(row=2, columnspan=8)
dec_lbl.grid(row=3, columnspan=8)
spacer_lbl.grid(row=4)

decbin_lbl.grid(row=5, columnspan=8)
dec_entry.grid(row=6, columnspan=8)
convbin_btn.grid(row=7, columnspan=8)
bin_lbl.grid(row=8, columnspan=8)

root.mainloop()
