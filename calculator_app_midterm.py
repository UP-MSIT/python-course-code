from tkinter import *

# Function to handle button clicks
def button_click(number):
    current = displayEntry.get()
    # Allowing only one dot in the input
    if number == "." and "." in current:
        return
    displayEntry.delete(0, END)
    displayEntry.insert(END, current + str(number))
    

# Function to handle addition
def button_add():
    global first_number
    first_number = float(displayEntry.get())
    displayEntry.delete(0, END)
    operation.set("+")

# Function to handle subtraction
def button_subtract():
    global first_number
    first_number = float(displayEntry.get())
    displayEntry.insert(END,'-')
    operation.set("-")

# Function to handle multiplication
def button_multiply():
    global first_number
    first_number = float(displayEntry.get())
    displayEntry.delete(0, END)
    operation.set("*")

# Function to handle division
def button_divide():
    global first_number
    first_number = float(displayEntry.get())
    displayEntry.delete(0, END)
    operation.set("/")

# Function to handle the equal button click
def button_equal():
    second_number = float(displayEntry.get())
    displayEntry.delete(END, operation.get())
    
    if operation.get() == "+":
        result = first_number + second_number
    elif operation.get() == "-":
        result = first_number - second_number
    elif operation.get() == "*":
        result = first_number * second_number
    elif operation.get() == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error: Division by zero"
    displayEntry.insert(0, str(result))

# Create the main window
main = Tk()
main.title("Calculator")
main.geometry('420x370+750+300')
main.resizable(0, 0)

displayEntry = Entry(main, font=('Arial', 12), width=50, border=2, justify="center")
displayEntry.place(x=0, y=0, height=50)

btnHeight = 3

# Row 1
yRow1 = 42
btnClear = Button(text="C", fg='Black', background='White', height=btnHeight, width=36)
btnClear.place(x=0, y=yRow1)

btnPlus = Button(text="+", fg='Black', background='White', height=btnHeight, width=9, command=button_add)
btnPlus.place(x=300, y=yRow1)

# Row 2
yRow2 = 106
btnOne = Button(text="1", fg='Black', background='White', height=btnHeight, width=9, command=lambda: button_click(1))
btnOne.place(x=0, y=yRow2)

btnTwo = Button(text="2", fg='Black', background='White', height=btnHeight, width=9, command=lambda: button_click(2))
btnTwo.place(x=100, y=yRow2)

btnThree = Button(text="3", fg='Black', background='White', height=btnHeight, width=9, command=lambda: button_click(3))
btnThree.place(x=200, y=yRow2)

btnSubtraction = Button(text="-", fg='Black', background='White', height=btnHeight, width=9, command=button_subtract)
btnSubtraction.place(x=300, y=yRow2)

# Row 3
yRow3 = 170
btnFour = Button(text="4", fg='Black', background='White', height=btnHeight, width=9, command=lambda: button_click(4))
btnFour.place(x=0, y=yRow3)

btnFive = Button(text="5", fg='Black', background='White', height=btnHeight, width=9, command=lambda: button_click(5))
btnFive.place(x=100, y=yRow3)

btnSix = Button(text="6", fg='Black', background='White', height=btnHeight, width=9, command=lambda: button_click(6))
btnSix.place(x=200, y=yRow3)

btnMultipy = Button(text="*", fg='Black', background='White', height=btnHeight, width=9, command=button_multiply)
btnMultipy.place(x=300, y=yRow3)

# Row 4
yRow4 = 234
btnSeven = Button(text="7", fg='Black', background='White', height=btnHeight, width=9, command=lambda: button_click(7))
btnSeven.place(x=0, y=yRow4)

btnEigth = Button(text="8", fg='Black', background='White', height=btnHeight, width=9, command=lambda: button_click(8))
btnEigth.place(x=100, y=yRow4)

btnNine = Button(text="9", fg='Black', background='White', height=btnHeight, width=9, command=lambda: button_click(9))
btnNine.place(x=200, y=yRow4)

btnDivision = Button(text="/", fg='Black', background='White', height=btnHeight, width=9, command=button_divide)
btnDivision.place(x=300, y=yRow4)

# Row 5
yRow5 = 298
btnZero = Button(text="0", fg='Black', background='White', height=btnHeight, width=24, command=lambda: button_click(0))
btnZero.place(x=0, y=yRow5)

btnDot = Button(text=".", fg='Black', background='White', height=btnHeight, width=9, command=lambda: button_click('.'))
btnDot.place(x=200, y=yRow5)

btnEqual = Button(text="=", fg='Black', background='White', height=btnHeight, width=9, command=button_equal)
btnEqual.place(x=300, y=yRow5)

# Variable to store the operation
operation = StringVar()

main.mainloop()