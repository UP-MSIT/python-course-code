from tkinter import *

main = Tk()
main.title = "Creating a Button Widget"
main.geometry('300x300+150+150')
main.resizable(0, 0)

# Create the button widget
cmd_Btn = Button(main, text='Click me', fg='Navy', bg='white')
cmd_Btn.place(x=130, y=130)

mainloop()