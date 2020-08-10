from tkinter import *
from os import chdir


root = Tk()
root.title("English")

def show_files():
	text_area.delete(1.0, END)
	


def open_file():
	try:
		arquivo = open(file_name_entry.get())
		content_file = "".join(arquivo.readlines())
		text_area.delete(1.0, END)
		text_area.insert(END,content_file)
		arquivo.close()
	except:

		def create_file():
			arquivo = open(file_name_entry.get(), "w")
			arquivo.close()
			new_window.destroy()

		def exit_new_window():
			new_window.destroy()

		alert_mensage = f"The file \"{file_name_entry.get()}\" does't exit"

		new_window = Toplevel()
		new_window.title("File does't exit")

		LabelCreatFile = Label(new_window, text=alert_mensage,)
		LabelCreatFile.grid(row=0,column=0,columnspan=2)

		button_confirm = Button(new_window, text="Creat the file",command= create_file)
		button_confirm.grid(row=1,column=0)

		button_not_confirm = Button(new_window, text="Don't creat the file",command=exit_new_window)
		button_not_confirm.grid(row=1,column=2)


def write_changes():
	file_name = file_name_entry.get()
	
	content = text_area.get("1.0", END)

	arquivo = open(file_name, "w")
	arquivo.write(content)
	arquivo.close()

def clear_text_area():
	text_area.delete(1.0, END)

def Save(event):
	if event.keysym == "s":
		print("Salvo com sucesso")
		arquivo = open(file_name_entry.get(), "w")
		arquivo.write(text_area.get(1.0,END))
		arquivo.close()
#Declaring

directory_entry = Entry(root)
file_name_label = Label(root, text="Write the name of file")
file_path_label = Label(root, text="Write the path that you want to work with")
file_name_entry = Entry(root)
text_area = Text(root, height=30,width=100, background="black",foreground="#0dff00",
	font=("monospace", 15),insertbackground="#0dff00", borderwidth=8, highlightbackground="red")


text_area.bind("<Control-s>", Save)

button_write_changes = Button(root, text="write changes", command=write_changes)
button_open = Button(root, text="open file", command=open_file)
button_clear = Button(root, text="clear text area", command=clear_text_area)

#Position
file_name_label.grid(row=1,column=0)
file_path_label.grid(row=0,column=0)
file_name_entry.grid(row=1,column=1)
directory_entry.grid(row=0,column=1)

text_area.grid(row=2,column=0,columnspan=4)

button_clear.grid(row=0, column=5)
button_open.grid(row=0,column=2)
button_write_changes.grid(row=0,column=3)

root.mainloop()
