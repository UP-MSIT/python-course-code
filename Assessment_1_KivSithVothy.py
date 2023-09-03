from tkinter import *

root = Tk()
root.title("Calculator")

bar = Entry(root, width=30, bd=4,font=("Ubuntu", 18, "normal",),fg="blue", bg="Pale Turquoise", justify=CENTER)
bar.place(x=0, y=0)

X = 85
Y = 90

w = 350
h = 400

# Get the screen dimensions
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

# Find the center of the point
cx = int(sw/2 - h/2)
cy = int(sh/2 - w/2)

root.geometry(f'{w}x{h}+{cx}+{cy}')
root.resizable(False, False)


def insert_number(number):
    bar['fg'] = "blue"
    text = bar.get()
    if (text.split() == []) and (number == "/" or number == "*" or number == ")"):
        number = ''
    elif (text.endswith('*')) and (number in ("+", "-", "/", "*")):
        backspace()
    elif (text.endswith('/')) and (number in ("+", "-", "/", "*")):
        backspace()
    elif (text.endswith('+')) and (number in ("+", "-", "/", "*")):
        backspace()
    elif (text.endswith('-')) and (number in ("+", "-", "/", "*")):
        backspace()
    elif (text.endswith('.')) and (number in (".", "+", "-", "/", "*")):
        number = ''
    bar.insert(END, number)


def backspace():
    bar['fg'] = "blue"
    try:
        text = bar.get()
        l = list(text)
        l.pop()
        text = "".join(l)
        bar.delete(0, END)
        bar.insert(0, text)
    except:
        pass


def delete():
    bar['fg'] = "blue"
    bar.delete(0, END)


def bracket_check():
    text = str(bar.get())
    Text = list(text)
    open_brackets = 0
    for char in Text:
        if char == "(":
            open_brackets += 1
        elif char == ")":
            open_brackets -= 1
    return open_brackets


def evaluate_expression():
    text = str(bar.get())

    open_brackets = bracket_check()
    if open_brackets > 0:
        bar.insert(END, ")" * open_brackets)
    else:
        try:
            answer = eval(text)
            delete()
            bar.insert(0, answer)
            bar['fg'] = "forestgreen"
        except:
            bar['fg'] = "red"


def insert_number_0():
    insert_number("0")


def insert_number_1():
    insert_number("1")


def insert_number_2():
    insert_number("2")


def insert_number_3():
    insert_number("3")


def insert_number_4():
    insert_number("4")


def insert_number_5():
    insert_number("5")


def insert_number_6():
    insert_number("6")


def insert_number_7():
    insert_number("7")


def insert_number_8():
    insert_number("8")


def insert_number_9():
    insert_number("9")


# Row 1
clear = Button(root, text="C", font=("Courier New", 16, "bold"),
               padx=105, pady=16, bd=4, bg="light cyan", command=delete)
clear.place(x=0, y=Y-50)

plus = Button(root, text="+", font=("Courier New", 16, "bold"), padx=20,
              pady=16, bd=4, bg="light cyan", command=lambda: insert_number("+"))
plus.place(x=3 * X, y=Y - 50)

# Row 2
n1 = Button(root, text="1", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
            command=insert_number_1)
n1.place(x=0, y=Y + 20)

n2 = Button(root, text="2", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
            command=insert_number_2)
n2.place(x=X, y=Y + 20)

n3 = Button(root, text="3", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
            command=insert_number_3)
n3.place(x=2 * X, y=Y + 20)

minus = Button(root, text="-", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
               command=lambda: insert_number("-"))
minus.place(x=3 * X, y=Y+20)

# Row 3
n4 = Button(root, text="4", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
            command=insert_number_4)
n4.place(x=0, y=(2 * Y))

n5 = Button(root, text="5", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
            command=insert_number_5)
n5.place(x=X, y=(2 * Y))

n6 = Button(root, text="6", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
            command=insert_number_6)
n6.place(x=2 * X, y=(2 * Y))

multiply = Button(root, text="*", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
                  command=lambda: insert_number("*"))
multiply.place(x=3 * X, y=(2 * Y))

# Row 4
n7 = Button(root, text="7", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
            command=insert_number_7)
n7.place(x=0, y=(3 * Y) - 20)

n8 = Button(root, text="8", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
            command=insert_number_8)
n8.place(x=X, y=(3 * Y) - 20)

n9 = Button(root, text="9", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
            command=insert_number_9)
n9.place(x=2 * X, y=(3 * Y) - 20)

divide = Button(root, text="/", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
                command=lambda: insert_number("/"))
divide.place(x=3 * X, y=(3 * Y) - 20)

# Row 5
n0 = Button(root, text="0", font=("Courier New", 16, "bold"), padx=60, pady=16, bd=4, bg="light cyan",
            command=insert_number_0)
n0.place(x=0, y=(3 * Y) + 50)

decimal = Button(root, text=".", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
                 command=lambda: insert_number("."))
decimal.place(x=2 * X, y=(3 * Y) + 50)

equal = Button(root, text="=", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
               command=evaluate_expression)
equal.place(x=3 * X, y=(3 * Y) + 50)

# back = Button(root, text="←", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="light cyan",
#               command=backspace)
# back.place(x=0, y=(4 * Y) + 20)

root.mainloop()
