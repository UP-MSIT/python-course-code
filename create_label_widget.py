from tkinter import *
main = Tk() #Creating Main Window
main.geometry('500x500')


def onButton_Click():
    lblWidget.configure(text="Congratulation! You can use command in button click now.")

lblWidget = Label(main, text = 'This is a Label widget using tkinter Library in Python', fg = 'Blue', bg = 'White')
lblWidget.place(x = 10, y = 20) # Set position of Label within win-form
cmd_Btn = Button(main, text = 'Click Me!', fg = 'Navy', bg = 'White', command=onButton_Click)
cmd_Btn.place(x = 130, y = 130)


lblUserName = Label(main, text = 'Username', fg = 'Blue')
lblUserName.place(x = 130, y = 160)
entryUserName = Entry(main, bd=2)
entryUserName.place(x = 130, y = 180)

lblUserName = Label(main, text = 'Password', fg = 'Blue')
lblUserName.place(x = 130, y = 160)
entryPassword = Entry(main, bd=2, show='*')
entryPassword.place(x = 130, y = 250)

mainloop()