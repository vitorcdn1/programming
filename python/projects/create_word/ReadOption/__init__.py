from random import randint, choice

import termcolor
import os
import platform

def clear():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

class Table:

	def __init__(self, palavra, char, num):

		self.char = char
		self.num = num
		self.palavra = palavra

	def ShowTitle(self):
		print(f"{self.char * self.num} {self.palavra} {self.char * self.num}")

	def CloseTitle(self):

		result = ((self.num * 2) + 2) + (len(self.palavra))
		print(self.char * result)

class ReadOption:

	def __init__(self, option = list()):
		self.option = option


	def ShowOption(self):
		if self.option != []:
			for c in range(0, len(self.option)):
				print(f"{c} - {self.option[c]}")

	def ReadOption(self, pergunta):

		if self.option == []:
			while True:
				num = input(pergunta)
				if num.isnumeric() == True:
					return int(num)
				else:
					clear()
					print(termcolor.colored("Error type a real number", "red"))
					break
		else:
			num_option = list()

			for c in range(0, len(self.option)):
				num_option.append(c)

			while True:
				num = input(pergunta)
				if num.isnumeric() == True:
					if int(num) in num_option:
						return int(num)
					else:
						clear()
						print(termcolor.colored("Error type a real option !!!", "red"))
						break
				else:
					clear()
					print(termcolor.colored("Error type a integer number !!!", "red"))
					break

def GeneratePass(tamanho = 10, lower = True, upper = True, num = True):

	alphabeto = "abcdefghijklmnopqrstuvwxyz"

	if lower == False and upper == False and num == False:
		print(termcolor.colored("Error all options are false"))

	else:
		return_list = list()
		size = len(return_list)

		while size != tamanho:

			while True:

				x = randint(0, 3)

				if x == 0:
					if lower == True:
						return_list.append(choice(alphabeto))
						break
				if x == 1:
					if upper == True:
						return_list.append(choice(alphabeto.upper()))
						break
				if x == 2:
					if num == True:
						return_list.append(str(randint(0, 9)))
						break

			size = len(return_list)

	return "".join(return_list)
