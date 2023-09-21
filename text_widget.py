import tkinter as tk

def scroll_textbar(*args):
    Txt.yview(*args)

root = tk.Tk()
root.geometry("300x200")

Txt = tk.Text(root, height=2, width=30)
Txt.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, command=scroll_textbar)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

Txt.config(yscrollcommand=scrollbar.set)
scroll_textbar("moveto", 0.0)

Txt.insert(tk.END, "Python tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFilePython tkinter widgetsFile")

tk.mainloop()
