from random import randint, choice
from os import system



alphabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def word(num=True,lower=True,upper=True):

	if num == False and lower == False and upper == False:
		print("ERROR !!!")
		print("All of the are false")

	return_list = list()

	

while True:
	
	system("clear")
	print("Write True or False to generate the word")
	num1 = bool(input("Do you want numbers: "))
	num2 = bool(input("Do you want uppercase: "))
	num3 = bool(input("Do you want lowercase: "))
	word(num1, num2, num3)
	input("press return to generate a new word...")
