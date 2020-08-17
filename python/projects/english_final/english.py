from tkinter import *
from tkinter.messagebox import showwarning, showinfo
from os import getcwd
<<<<<<< Updated upstream

=======
 
>>>>>>> Stashed changes
root = Tk()
root.title("English")


def search():

	text.config(state=NORMAL)
	print("search()")

	try:

		text.delete(1.0, END)
		arquivo = open(entry_search.get(), "r")
		content = arquivo.readlines()
		arquivo.close()

		for c in content:
			text.insert(END, c)

	except:
		showwarning(title=f"word {entry_search.get()}",message=f"word {entry_search.get()} does't exist")
		print("error")

	text.config(state=DISABLED)

def edit():
	text.config(state = NORMAL)

	print("edit()")

	text.delete(1.0, END)

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
	try:
		arquivo = open(entry_search.get(), "r+")

		content = arquivo.readlines()

		for c in content:
			text.insert(END, C)

		arquivo.close()
	except:

		showwarning(title="Edit" ,message=f"The file {entry_search.get()} will be created and ready for edit")
		arquivo = open(entry_search.get(), "w")
		arquivo.close()
		print("erro")

def save():

	content = text.get(1.0, END)

	arquivo = open(entry_search.get(), "r+")

	arquivo.writelines(content)

	arquivo.close()

	showinfo(title="save", message="file saved")
# Label

#Button

button_exit = Button(root, text = "Exit the program",command = root.quit)
button_search = Button(root, text = "Search", command = search)
button_edit = Button(root, text = "Edit", command = edit)
button_save = Button(root, text="Save", command= save)

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
button_save.grid(row=0, column=3)

root.mainloop()
