from tkinter import *

root = Tk()

work_place_label = Label(root, text="Path place")
work_place_entry = Entry(root)

#Position
work_place_label.grid(row=0, column=0)
work_place_entry.grid(row=0, column=1)

root.mainloop()
