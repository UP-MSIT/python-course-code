from tkinter import *
from tkinter.ttk import Combobox
winFrm=Tk()

# Title Answer Labels in TOP of the window form
lbl_result = Label(winFrm, text='Display Result ...',font= ('Arial', 14, 'normal'),fg='navy', bg='lightgrey', width=100, height=5, justify="center")
lbl_result.pack(side=TOP)
v=IntVar()
v.set(1)      # initializing the choice, i.e. Python
languages=[("Python Programming", 101),("Perl Programming", 102),("Java Programming", 103),("C++ Programming", 104),("C Programming", 105)]
def ShowChoice():
    result = v.get ()
    if (v.get()==101):
        lbl_result.config(text = '''Python is an interpreted, object-oriented,
high-level programming language with
dynamic semantics.''')
    elif (result == 102):
        lbl_result.config(text = '''Perl is a high-level general-purpose
programming language used especially for
developing Web applications.''')
    elif (result == 103) :
        lbl_result.config(text = '''Java is a multi-platform, object-oriented,
and network-centric language that can be used as a platform in itself.''')
    elif (result == 104):
        lbl_result.config(text = '''C++ is an object-oriented programming
language which gives a clear structure to programs and allows
code to be reused, lowering development costs.''')
    elif (result == 105):
        lbl_result.config(text = '''C is a general-purpose computer programming
    language. It was created in the 1970s by Dennis Ritchie, and
    remains very widely used and influential.''')
    else:
        lbl_result.config(text = 'No Result...')
Label(winFrm,text="""what is your favourite programming language?""",font=('Arial',14,'normal'), justify=LEFT, bg='lightblue',width=100, padx=5, pady=10).pack()
for language, val in languages:
    Radiobutton(winFrm,text = language,padx = 50, pady = 7,variable = v,command = ShowChoice,value = val).pack(anchor = W)
#winIcon = PhotoImage (file = "good icon.png")
#winFrm.iconphoto (False, winIcon)
winFrm.title('Selection Widgets')
winFrm.geometry("550x345")
winFrm.resizable(False, False)
winFrm.mainloop()
