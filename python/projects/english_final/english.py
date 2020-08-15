from tkinter import *
from tkinter.messagebox import showwarning
from os import getcwd

root = Tk()
root.title("English")


def search():
	print("search()")

	try:

		text.delete(1.0, END)
		arquivo = open(entry_search.get(), "r")
		content = arquivo.readlines()
		arquivo.close()

		for c in content:
			text.insert(END, c)

		text.config(state=DISABLED)

	except:
		showwarning(title=f"word {entry_search.get()}",message=f"word {entry_search.get()} does't exist")
		print("error")

def edit():
	print("edit()")

	text.delete(1.0, END)

	try:
		arquivo = open(entry_search.get(), "r+")

		content = arquivo.readlines()

		for c in content:
			text.insert(END, C)

		arquivo.close()
	except:
		print("erro")
# Label

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

button_exit.grid(row=3,column=0, pady = 20)
button_search.grid(row=1,column=0, pady = 20)
button_edit.grid(row=1,column=1, pady = 20)

root.mainloop()
