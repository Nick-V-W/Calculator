from tkinter import *

root = Tk()
root.title("NickCalculator")
# this one is good because its settings aren't changed :)
screen = Entry(root, width=45, borderwidth=5)
screen.grid(row=0, column=0, columnspan=3)
information = []
smallerInfo = 0


def s_index_finder():
    word = len(screen.get())
    return word


def index_word():
    word = screen.get()[smallerInfo:s_index_finder()]
    return word


def click(n):
    global smallerInfo
    if n == 1:
        screen.insert(s_index_finder(), "1")
        operations_enable()
        bN.config(state="disabled")
    elif n == 2:
        screen.insert(s_index_finder(), "2")
        operations_enable()
        bN.config(state="disabled")
    elif n == 3:
        screen.insert(s_index_finder(), "3")
        operations_enable()
        bN.config(state="disabled")
    elif n == 4:
        screen.insert(s_index_finder(), "4")
        operations_enable()
        bN.config(state="disabled")
    elif n == 5:
        screen.insert(s_index_finder(), "5")
        operations_enable()
        bN.config(state="disabled")
    elif n == 6:
        screen.insert(s_index_finder(), "6")
        operations_enable()
        bN.config(state="disabled")
    elif n == 7:
        screen.insert(s_index_finder(), "7")
        operations_enable()
        bN.config(state="disabled")
    elif n == 8:
        screen.insert(s_index_finder(), "8")
        operations_enable()
        bN.config(state="disabled")
    elif n == 9:
        screen.insert(s_index_finder(), "9")
        operations_enable()
        bN.config(state="disabled")
    elif n == 0:
        screen.insert(s_index_finder(), "0")
        bN.config(state="disabled")
        operations_enable()
    # this is handling how to deal with a negative sign when pressing the button
    elif n == "-":
        if len(index_word()) == 0:
            screen.insert(s_index_finder(), "-")
            bN.config(state="disabled")
            bLP.config(state="disabled")
            bRP.config(state="disabled")
        else:
            return
    # this is handling how to deal with a decimal when pressing the button
    elif n == "." and index_word().find(".") == -1:
        screen.insert(s_index_finder(), ".")
        bO.config(state="disabled")
        bN.config(state="disabled")
        bLP.config(state="disabled")
        bRP.config(state="disabled")
    else:
        if smallerInfo != 0:
            smallerInfo = 0
        screen.delete(0, END)
        num_buttons_enable()
        bE.config(state="disabled")
        bD.config(state="disabled")
        bM.config(state="disabled")
        bS.config(state="disabled")
        bP.config(state="disabled")
        bLP.config(state="normal")
        bRP.config(state="normal")
        information.clear()


def calc_function(x):
    global smallerInfo
    if x == "+":
        information.append(float(index_word()))
        information.append("+")
        screen.insert(s_index_finder(), "+")
        smallerInfo = s_index_finder()
        bO.config(state="normal")
        bN.config(state="normal")
        operations_disable()
    elif x == "-":
        information.append(float(index_word()))
        information.append("-")
        screen.insert(s_index_finder(), "-")
        smallerInfo = s_index_finder()
        bO.config(state="normal")
        bN.config(state="normal")
        operations_disable()
    elif x == "*":
        information.append(float(index_word()))
        information.append("*")
        screen.insert(s_index_finder(), "*")
        smallerInfo = s_index_finder()
        bO.config(state="normal")
        bN.config(state="normal")
        operations_disable()
    elif x == "/":
        information.append(float(index_word()))
        information.append("/")
        screen.insert(s_index_finder(), "/")
        smallerInfo = s_index_finder()
        bO.config(state="normal")
        bN.config(state="normal")
        operations_disable()
    elif x == "(":
        screen.insert(s_index_finder(), "(")
        if screen.get()[s_index_finder() - 2] in "1234567890":
            information.append(float(index_word()))
            information.append("*")
            information.append("(")
        elif screen.get()[s_index_finder() - 2] == "(":
            information.append("*")
            information.append("(")
        else:
            information.append("(")
        smallerInfo = s_index_finder()
        bRP.config(state="disabled")
    elif x == ")":
        print("f")
        # ADDDDDDD )) BUTTON HERE

        # lol
        # hahahaha




    # ADDDDDD )) BUTTON HERE
    else:
        return


def operations_disable():
    bE.config(state="disabled")
    bM.config(state="disabled")
    bD.config(state="disabled")
    bP.config(state="disabled")
    bS.config(state="disabled")


def operations_enable():
    bE.config(state="normal")
    bM.config(state="normal")
    bD.config(state="normal")
    bP.config(state="normal")
    bS.config(state="normal")
    bLP.config(state="normal")
    bRP.config(state="normal")


def button_disable():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")
    b7.config(state="disabled")
    b8.config(state="disabled")
    b9.config(state="disabled")
    b0.config(state="disabled")
    bE.config(state="disabled")
    bM.config(state="disabled")
    bS.config(state="disabled")
    bP.config(state="disabled")
    bD.config(state="disabled")
    bN.config(state="disabled")
    bO.config(state="disabled")


def num_buttons_enable():
    b1.config(state="normal")
    b2.config(state="normal")
    b3.config(state="normal")
    b4.config(state="normal")
    b5.config(state="normal")
    b6.config(state="normal")
    b7.config(state="normal")
    b8.config(state="normal")
    b9.config(state="normal")
    b0.config(state="normal")
    bN.config(state="normal")
    bO.config(state="normal")


def add_subtract(info, w):
    while len(info) > 1:
        if info[w] == "+":
            result2 = float(info[w - 1]) + float(info[w + 1])
            info.remove(info[w + 1])
            info.remove(info[w])
            info.remove(info[w - 1])
            info.insert(w - 1, result2)
        elif info[w] == "-":
            result3 = float(info[w - 1]) - float(info[w + 1])
            info.remove(info[w + 1])
            info.remove(info[w])
            info.remove(info[w - 1])
            info.insert(w - 1, result3)
    return info


def multiply_divide(info, w):
    if info[w] == "*":
        result = float(info[w - 1]) * float(info[w + 1])
        info.remove(info[w + 1])
        info.remove(info[w])
        info.remove(info[w - 1])
        info.insert(w - 1, result)
        if len(info) > 1:
            return multiply_divide(info, w)
    elif info[w] == "/" and info[w + 1] != 0:
        result1 = float(info[w - 1]) / float(info[w + 1])
        info.remove(info[w + 1])
        info.remove(info[w])
        info.remove(info[w - 1])
        info.insert(w - 1, result1)
        if len(info) > 1:
            return multiply_divide(info, w)
    elif info[w] == "/" and info[w + 1] == 0:
        info.clear()
        info.append("Cannot divide by zero :(")
    elif len(info) > 1 and w != len(info) - 2:
        w += 2
        return multiply_divide(info, w)
    else:
        return info


def equals():
    global information
    information.append(float(index_word()))
    screen.insert(s_index_finder(), " =")
    w = 1
# this is for just addition and subtraction
    if (information.count("+") > 0 or information.count("-") > 0) and information.count("*") == 0 \
            and information.count("/") == 0:
        information = add_subtract(information, w)
# this is for just multiplication and division
    elif (information.count("*") > 0 or information.count("/") > 0) and information.count("+") == 0 \
            and information.count("-") == 0:
        information = multiply_divide(information, w)
# this is for combinations of (addition or subtraction) and (multiplication or division)
    elif (information.count("+") > 0 or information.count("-") > 0) and (information.count("*") > 0
                                                                         or information.count("/") > 0):
        information = multiply_divide(information, w)
        w = 1
        information = add_subtract(information, w)
    answer = " " + str(information[0])
    # removes unnecessary .0 at the end of answers EX: 1.0 becomes 1 lol
    if answer.find(".0", 0) == len(answer) - 2:
        answer = answer.replace(".0", "")
        information.clear()
        information.append(answer)
    print(information)
    button_disable()
    screen.insert(s_index_finder(), information[0])
    information.clear()


# creating buttons
b1 = Button(root, text="1", padx=50, pady=2, command=lambda: click(1))
b2 = Button(root, text="2", padx=50, pady=2, command=lambda: click(2))
b3 = Button(root, text="3", padx=50, pady=2, command=lambda: click(3))
b4 = Button(root, text="4", padx=50, pady=2, command=lambda: click(4))
b5 = Button(root, text="5", padx=50, pady=2, command=lambda: click(5))
b6 = Button(root, text="6", padx=50, pady=2, command=lambda: click(6))
b7 = Button(root, text="7", padx=50, pady=2, command=lambda: click(7))
b8 = Button(root, text="8", padx=50, pady=2, command=lambda: click(8))
b9 = Button(root, text="9", padx=50, pady=2, command=lambda: click(9))
b0 = Button(root, text="0", padx=50, pady=2, command=lambda: click(0))
bC = Button(root, text="Clear", padx=97, pady=2, command=lambda: click("c"))
bN = Button(root, text="(-)", padx=46, pady=2, command=lambda: click("-"))
bO = Button(root, text=".", padx=52, pady=2, command=lambda: click("."))
bLP = Button(root, text="(", padx=51, pady=2, command=lambda: calc_function("("))
bRP = Button(root, text=")", padx=51, pady=2, command=lambda: calc_function(")"))

bE = Button(root, text="=", padx=49, pady=2, state=DISABLED, command=equals)
bP = Button(root, text="+", padx=49, pady=2, state=DISABLED, command=lambda: calc_function("+"))
bS = Button(root, text="-", padx=51, pady=2, state=DISABLED, command=lambda: calc_function("-"))
bD = Button(root, text="/", padx=51, pady=2, state=DISABLED, command=lambda: calc_function("/"))
bM = Button(root, text="*", padx=51, pady=2, state=DISABLED, command=lambda: calc_function("*"))
update = Label(root, text="NickCalculator Ver. 2.0.0 (Parentheses update coming soon!)")
# patch = Label(root, text="Ver. 2.5.1 Patch Notes:\n
# -Fixed issue where dividing by zero would crash the calculator\n-Implemented parentheses\n
# -Added version info at the bottom of the window\n-Added patch notes section\n-Optimized code, justify=LEFT)

# placing buttons
bD.grid(row=0, column=3)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
bM.grid(row=1, column=3)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
bS.grid(row=2, column=3)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
bP.grid(row=3, column=3)
b0.grid(row=4, column=0)  # what
bO.grid(row=4, column=1)
bN.grid(row=4, column=2)
bE.grid(row=4, column=3)
bLP.grid(row=5, column=0)
bRP.grid(row=5, column=1)
bC.grid(row=5, column=2, columnspan=2)
update.grid(row=6, columnspan=4)
# patch.grid(column=4, columnspan=2, row=0, rowspan=4)
root.mainloop()
# before update 2.5.1, program was 350 lines of code long
