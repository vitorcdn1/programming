from tkinter import *


root = Tk()
root.geometry(("500x500"))
root.title("English")

def search():
	print("search()")

def edit():
	print("edit()")
button_exit = Button(root, text = "Exit the program",command = root.quit)
button_search = Button(root, text = "Search", command = search)
button_edit = Button(root, text = "Edit", command = edit)
entry_search = Entry(root)


entry_search.grid(row=0,column=0,columnspan=2)
button_exit.grid(row=0,column=2)
button_search.grid(row=1,column=0)
button_edit.grid(row=1,column=1)

root.mainloop()
