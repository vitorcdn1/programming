from tkinter import *

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


person1 = Person("Vitor",15)
print(person1.name)
