from tkinter import *
from english_functions.path_fun import *
from os import getcwd

root = Tk()
root.title("English")


def search():
	print("search()")

	arquivo = open(".default.txt", "w")
	chdir(arquivo.readlines())
	arquivo.close()
	try:
		root.title(entry_search.get())
		arquivo = open(entry_search.get())
		
		content = arquivo.readlines()
		arquivo.close()

		print(content)
	except:
		print(f"The file {entry_search.get()} does't exist")

def edit():
	print("edit()")

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

root.after(1000, check_if_default_file_exist())

root.mainloop()
