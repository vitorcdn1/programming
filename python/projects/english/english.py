from tkinter import *
from os import chdir

def create_new_window(menssage="Do you want to create a new window",):

	window = Toplevel()
	window.title("Create a new File")

	text = Label(window, text=menssage)
	button_confirm = Button(window, text="Confirm")
	button_cancel = Button(window, text="Cancel", command= window.quit)
	

	text.grid(row=0, column=0,columnspan=3)

def current():
	try:
		arquivo = open(".default", r+)

	except:
		default_path = "/home/vitor/"
		arquivo = open(".default.txt", "w")

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
