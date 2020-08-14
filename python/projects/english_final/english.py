from tkinter import *


root = Tk()
root.geometry(("700x500"))
root.title("English")

def search():
	print("search()")

def edit():
	print("edit()")

#Button

button_exit = Button(root, text = "Exit the program",command = root.quit)
button_search = Button(root, text = "Search", command = search)
button_edit = Button(root, text = "Edit", command = edit)

# Input
text = Text(root, height=20, width=80)
entry_search = Entry(root)

# Inputs position

entry_search.grid(row=0,column=0,columnspan=2)
text.grid(row = 2, column = 0 , columnspan = 3)
# Button position

button_exit.grid(row=3,column=1)
button_search.grid(row=1,column=0)
button_edit.grid(row=1,column=1)

root.mainloop()
