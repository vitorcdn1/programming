from tkinter import *
from os import chdir

root = Tk()
	root.title("English")

# Widgets
work_place_label = Label(root, text="Path place: ")
work_place_entry = Entry(root)
file_text_area = Text(root, width=50, height=20)

#Position
work_place_label.grid(row=0, column=0)
work_place_entry.grid(row=0, column=1)
file_text_area.grid(row=1, column=0, columnspan=2)

root.mainloop()
