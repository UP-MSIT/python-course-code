from tkinter import *


def motion(event):
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return


master = Tk()
master.geometry("400x250")
sms_info = "Today's AI have arrived as compared to the expert system's of the past."
msg = Message(master, text=sms_info)
msg.config(bg='lightyellow', font=('Arial', 24, 'normal'))
msg.bind('<Motion>', motion)
msg.pack()
mainloop()
