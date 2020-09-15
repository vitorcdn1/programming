from random import randint, choice
from termcolor import colored
from os import system
import platform

def clear():

	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

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
	
	clear()
	print(f"{'-'*10} Create Random Words  {'-'*10}")
	print("Write (yes/no) to generate the word")

	lower = ReadYesNo("Do you want LowerCase in your password: ")
	upper = ReadYesNo("Do you want UpperCase in your password: ")
	numbers = ReadYesNo("Do you want numbers in your password: ")

	word(lower, upper, numbers)
	input("press return to generate a new word...")
