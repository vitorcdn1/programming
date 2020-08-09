from tkinter import *
from getpass import getuser, getpass
from os import chdir, system

def create_new_window(menssage="Do you want to create a new window",): # Create a new window

	def Create_file(FileName="teste.txt"):

		arquivo = open(FileName, "w")
		arquivo.close()

	window = Toplevel()
	window.title("Create a new File")

	text = Label(window, text=menssage)
	button_confirm = Button(window, text="Confirm", command= lambda: Create_file(".default.txt"))
	button_cancel = Button(window, text="Cancel", command= window.quit)

	button_cancel.grid(row=1,column=0)
	button_confirm.grid(row=1, column=2)
	text.grid(row=0, column=0,columnspan=3)

def current_path():
	try:
		arquivo = open(".default", "r+")

		content = arquivo.readlines()

		if len(content) > 5:
			chdir(content)

		system("ls")

	except:
		default_path = "/home/" + getuser() + "/"
		
		print(default_path)
		create_new_window("The config file \".default.txt\" does't exit do you want to create")


def save_file():

	content = file_text_area.get("1.0", END)
	

root = Tk()
root.title("English")

# Widgets
work_place_label = Label(root, text="Path place: ")
work_place_entry = Entry(root)
file_text_area = Text(root, width=50, height=20)
button_save = Button(root, text="Save that file", command= save_file)


#Position
work_place_label.grid(row=0, column=0)
work_place_entry.grid(row=0, column=1)
file_text_area.grid(row=2, column=0, columnspan=2)
button_save.grid(row=1,column=0)

root.mainloop()
