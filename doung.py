from tkinter import *
from tkinter.ttk import Combobox
class CalcWinFrm:
    def __init__ (self, win):
        # Design 4 Labels in the window form
        self.lbl_calc=Label(win, text='Calculator Application - Tkinter UI', font= ('Arial', 16, 'bold'), fg='navy', bg='lightgrey', width=100, height=2, justify='center')
        self.lbl_1st_op=Label(win, text='First number', font= ('Arial', 10, 'bold'), bg='lightgrey', width=19)
        self.lbl_2nd_op=Label(win, text=' Second number',  font= ('Arial', 10, 'bold'), bg='lightgrey', width=19)
        self.lbl_Results=Label(win, text='Results',  font= ('Arial', 10, 'bold'),  bg='lightgrey', width=19)
        # Create 3 Entry box in the window form
        self.entry_1st_num=Entry(width=14, font=('Arial', 14, 'normal'), justify='right')
        self.entry_2nd_num=Entry(width=14, font= ('Arial', 14, 'normal'), justify= 'right')
        self.entry_result_num=Entry (width=14, font= ('Arial', 14, 'bold'), justify='left')
        # Create 4 Buttons in the window form
        self.btn_add = Button (win, text='+', width=3, command=self.add)
        self.btn_sub = Button (win, text='-', width=3, command=self.sub)
        self.btn_mul = Button (win, text='x', width=3, command=self.multi)

        self.btn_dev = Button (win, text='/', width=3, command=self.devi)
        # Set Title Label position in the TOP of window form
        self.lbl_calc.pack(side=TOP)
        # Set 3 Labels position in the window form
        self.lbl_1st_op.place (x=30, y=80)
        self.lbl_2nd_op.place(x=200, y=80) 
        self.lbl_Results.place (x=370, y=80)
        # Set 3 Entry Box position in the window form
        self.entry_1st_num.place(x=30, y=105)
        self.entry_2nd_num.place(x=200, y=105)
        self.entry_result_num.place(x=370, y=105)
        # Set 4 Buttons position in the window form
        self.btn_add.place (x=202, y=150)
        self.btn_sub.place (x=244, y=150) 
        self.btn_mul.place (x=288, y=150)
        self.btn_dev.place (x=330, y=150)
    # Create add () function 
    def add(self):
        self.entry_result_num.configure (state="normal")
        self.entry_result_num.delete (0, 'end')
        num1=float(self.entry_1st_num.get())
        num2=float(self.entry_2nd_num.get () )
        result = num1+num2
        self.entry_result_num.insert (END, str (float (result) ))
        self.entry_result_num.configure (state="disabled")

    #Create sub () function 
    def sub (self):
        self.entry_result_num.configure (state="normal")
        self.entry_result_num.delete (0, 'end')
        num1=float (self.entry_1st_num.get () )
        num2=float (self.entry_2nd_num.get () ) 
        result=num1-num2
        self.entry_result_num.insert (END, str (float (result)))
        self.entry_result_num.configure (state="disabled")
    # Create multi () function
    def multi (self):
        self.entry_result_num. configure (state="normal")
        self.entry_result_num.delete (0, 'end') 
        num1=float (self.entry_1st_num.get () )
        num2=float (self.entry_2nd_num.get () )
        result=num1*num2
        self.entry_result_num.insert (END, str (float (result)))
        self.entry_result_num.configure (state="disabled")
    # Create devi () function
    def devi (self):
        self.entry_result_num.configure (state="normal")
        self.entry_result_num.delete (0,
        'end')
        num1=float(self.entry_1st_num.get())
        num2=float (self.entry_and_num.get () )
        if (num2 !=0):
            result=num1/num2
            self.entry_result_num.insert(END, str (float (result) ))
        else:
           self.entry_result_num.insert (END, str ('Error!'))
           self.entry_result_num.configure (state="disabled")

# Create a window form
WinFrm=Tk()
width=555
# Set the width of the window form
height=200
# Set the Hight of the window form

# Call class of CalcWinFrm
mywin=CalcWinFrm(WinFrm)

# Set custom icon to window form
#photo = Photolmage (file = 'good icon.png')
#WinFrm.wm_iconphoto (False, photo)

# Set a new title of window form
WinFrm.title ('Python Calculator Application')

# Display window form in the central of computer screen
screen_width = WinFrm.winfo_screenwidth () # width of the screen
screen_height = WinFrm.winfo_screenheight () # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

# WinFrm.geometry ('$dx$d+%d+%d+%d' % (width, height, x, y) )

WinFrm. geometry('%dx%d+%d+%d' % (width, height, x, y))

#WinFrm.geometry ("555x200")

WinFrm. resizable (False, False)

WinFrm.mainloop ()