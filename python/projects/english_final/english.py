from tkinter import *


root = Tk()
root.geometry(("500x500"))
root.title("English")


button_exit = Button(root, text="Exit the program",command=root.quit)
button_exit.grid(row=0,column=0)

root.mainloop()