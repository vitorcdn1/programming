import termcolor
import os


class ReadOption:

	def __init__(self, option):
		os.system("clear")
		self.option = option

	def PrintOption(self):
		print("="*50)
		biggest = 0
		for c in range(0,len(self.option)):
			print(f"{c} - {self.option[c]}")
		print("="*50)

	def ReadOption(self, question):

		num_options = []

		if len(self.option) >= 1:
			for c in range(0,len(self.option)):
				num_options.append(str(c))

			while True:
				responce = input(question)

				if responce.isnumeric() == True:

					if responce in num_options:
						return int(responce)
					else:
						os.system("clear")
						print(termcolor.colored("Error Please type a valid option !!!!", "red"))
						break

				else:
					os.system("clear")
					print(termcolor.colored("Error Please Type a number !!!!", "red"))
					break
					

class Calculations(ReadOption):
	def __init__(self, option):
		self.option = option

	def ShowMultipleTable(self):

		os.system("clear")
		print(f"{'='*50} Multiple Table {'='*50}")

		while True:
			num_multiple = ReadOption("Digite uma tabuada: ")

			print(f"{'='*50} Multiple Table of {num_multiple} {'='*50}")

			for c in range(0,10):
				print(f"{num_multiple} X {c} = {num_multiple * c}")
	if option == 1:
		ShowMultipleTable()
while True:
	question = ReadOption(["Sair do programa","Mostrar uma tabuada"]) # Inicia a class ReadOption

	question.PrintOption() 						  # Print the options

	responce = question.ReadOption("Type a option: ") 		  # 
	conta = Calculations(responce)
	if responce == 0:
		break
	else:
		conta = Calculations(responce)

		
