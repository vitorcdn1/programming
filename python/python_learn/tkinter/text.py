from tkinter import *
import platform
import os

def clear():

	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

def show():
	print("I'm in")
	content = text.get("1.0", END)

	if content == "vitor nascimento\n":
		print("hey")

	root.after(1000, show)

root = Tk()

root.title("Learn style and text")

def test():
	content = text.get("1.0", END)
	print(content)

text = Text(root, width=50,height = 20, borderwidth=2)
text.pack()

button = Button(root, text="Click me", command=test)
button.pack()


show()
root.mainloop()
