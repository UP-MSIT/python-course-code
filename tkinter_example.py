from tkinter import *

main = Tk()
# main.geometry('1200x800')

# Example of calculation the center of the coordinate based on the screen and window width and height
main.title("TKinter Panel")
main.configure(bg = 'lightgreen')

w = 800
h = 600

# Get the screen dimensions
sw = main.winfo_screenwidth()
sh = main.winfo_screenheight()

# Find the center of the point
cx = int(sw/2 - h/2)
cy = int(sh/2 - w/2)

main.geometry(f'{w}x{h}+{cx}+{cy}')
main.resizable(False, False)

main.protocol("WM_DELETE_WINDOW",main)
# main.attributes("-fullscreen",1)

# Creating a Button widget
cmd_btn = Button(main, text="Click", fg='red', bg='white')

# Set position of Button within win-form
cmd_btn.place(x=130,y=130)

# Creating a Button widget
lbl_widget = Label(main, text="This is a Label widget using tkinter Library",fg="black",bg="white")
lbl_widget.place(x=230,y=240)
mainloop()
