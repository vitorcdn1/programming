from tkinter import *
from os import chdir

def WhereYouGonnaWork():
	
	def submit():
		chdir(work_place.get())
		chdir(Project_Place.get())


	WorkPlace = Toplevel()
	WorkPlace.title("Select Your Work place")

	# declaring

	Work_Place_Label = Label(WorkPlace, text="What's the directory you gonna work with ??")
	work_place = Entry(WorkPlace)

	Project_Place_Label = Label(WorkPlace, text="What project you're working with ??")
	Project_Place = Entry(WorkPlace)

	button_submit = Button(WorkPlace, text="Submit", command= submit)

	# Position

	Work_Place_Label.grid(row=0,column=0)
	work_place.grid(row=0,column=1)

	Project_Place_Label.grid(row=1,column=0)
	Project_Place.grid(row=1,column=1)
	button_submit.grid(row=2,column=0,columnspan=2)

	WorkPlace.mainloop()

root = Tk()
root.title("Learn English")

WhereYouGonnaWork()


root.mainloop()