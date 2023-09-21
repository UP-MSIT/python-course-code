from tkinter import *
from tkinter.ttk import *

main = Tk()
main.title = "Create Label Checkbox and Button"
main.geometry("480x230+230+100")

lbl_info = Label(main, text="Select the Month: ", font=("Times New Roman", 10))
lbl_info.place(x=50, y=50)

n = StringVar()
select_month = Combobox(main, width=27, state="readonly", textvariable=n)
select_month.place(x=50, y=80)

# Adding combobox deop down list
select_month['value'] = ('', 'Jan', 'Feb', 'Mar', 'Apr',
                         'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
select_month.current(0)
select_month.set("Pick an Option")

Button(main, text="Exit", command=main.destroy).place(x=50, y=120)

main.mainloop()
