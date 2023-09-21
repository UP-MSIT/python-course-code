from tkinter import *
from tkinter.ttk import *

main = Tk()
main.title = "Create Label Checkbox and Button"
main.geometry("480x130+230+100")


# Creating 2 Checkboxes
var1 = IntVar()
var2 = IntVar()
lbl_info = Label(main,text="Capital city and Tour Site")
lbl_info.place(x=80,y=15)


def var_state():
    # lbl_info.configure(text="Capital city: {} and Tour Site: {}" % (var1.get(), var2.get()))
    lbl_info.configure(text="Capital city: {} and Tour Site: {}".format(var1.get(), var2.get()))

chk1 = Checkbutton(main, text="Phnom Penh", variable=var1).place(x=80,y=50)
chk2 = Checkbutton(main, text="Siem Reap", variable=var2).place(x=200,y=50)

btn_show= Button(main, text="Show", command=var_state).place(x=80,y=80)
btn_exit= Button(main, text="Exit", command=main.destroy).place(x=200,y=80)

main.mainloop()