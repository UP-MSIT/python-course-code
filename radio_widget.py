from tkinter import *
from tkinter.ttk import *

main = Tk()

main.title("Create 3 Radio Button")
main.geometry("480x130+230+100")

# Create Radio Button
val = IntVar()
val.set(1)

rdo1 = Radiobutton(main, text="PhnomPenhh",variable=val, value=1)
rdo2 = Radiobutton(main, text="Siem Reap",variable=val, value=2)
rdo3 = Radiobutton(main, text="Battam Bang",variable=val, value=3)

rdo1.place(x=80, y=50)
rdo2.place(x=200, y=50)
rdo3.place(x=300, y=50)

main.mainloop()