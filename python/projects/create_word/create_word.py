from random import randint, choice
from termcolor import colored
import os
import platform
from ReadOption import Table, ReadOption

def clear():

	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

clear()

alphabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def word(num=True,lower=True,upper=True):

	if num == False and lower == False and upper == False:
		print(colored("ERROR !!! All of the are false", "red"))

	return_list = list()

	
def ReadYesNo(question):

	while True:

		result = input(question)
		if result == "yes":
			return True
		elif result == "no":
			return False
		else:
			error_menssage = colored("Error do you type (yes/no)", 'red')
			print(error_menssage)

while True:
	
	table = Table("Create random password and phrases", "=", 10)
	option = ReadOption([
		"Exit program",
		"Generate random phrase"
	])

	table.ShowTitle()

	option.ShowOption()

	table.CloseTitle()

	responce = option.ReadOption("Type a option: ")

	if responce == 0:
		break