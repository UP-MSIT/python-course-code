from tkinter import *
from tkinter import messagebox, ttk


main = Tk()
main.title = "Create Label Checkbox and Button"
main.geometry("480x430+230+100")


def show_msBox_dbl_clicked():
    indices = listbox.curselection()
    messagebox.showinfo(title="Selected Items", message=",".join(
        "Listbox[" + str(indices[0]) + "]=" + listbox.get(i) for i in indices))


def get_btn_clicked(event):
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_index = selected_indices[0]
        selected_item = listbox.get(selected_index)
        # print("Selected index: ", selected_index)

        messagebox.showinfo(title="Selected item", message=selected_item)


def show_selected(event):
    lbl_title.config(text=listbox.get(ANCHOR))


lbl_title = Label(main, font=("Times New Roman", 14, "bold"), fg='Red')
lbl_title.place(x=50, y=10)


frame = ttk.Frame()
listbox = Listbox()

scrollbar = ttk.Scrollbar(frame, orient=VERTICAL)

listbox = Listbox(frame, yscrollcommand=scrollbar.set, height=15)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack()
listbox.bind('<Double-1>', show_msBox_dbl_clicked)
listbox.bind('<<ListboxSelect>>', show_selected)
frame.place(x=50, y=40)

get_selected_btn=ttk.Button(text="Get selection", width=22)
get_selected_btn.place(x=50, y=290)
get_selected_btn.bind('<Button-1>', get_btn_clicked)

# Insert 100 items.

for i in range(1,101):
    listbox.insert(END, f"Items number {i}")


main.mainloop()
