import os
import termcolor
import platform

def clear():
	if platform.system() == "Linux":
		os.system("clear")
	else:
		os.system("cls")

clear()


class Table:
	def __init__(self, name, letra, num):
		self.name = name
		self.letra = letra
		self.num = num

	def ShowTitle(self):
		print(f"{self.letra * self.num} {self.name} {self.letra * self.num}")

	def CloseTitle(self):
		result = (2 + len(self.name)) + (self.num * 2)
		print(self.letra*result)
		

class ReadOption:
	
	def __init__(self, option):

		clear()

		self.option = option

	def ShowOptions(self):
		for c in range(0,len(self.option)):
			print(f"{c} - {self.option[c]}")

	def ReadOption(self, pergunta):
		while True:
			responce = input(pergunta)

			if responce.isnumeric() == True:
				
				if self.option == []:
					return int(responce)
				else:
					numlist = list()
					for c in range(0, len(self.option)):
						numlist.append(str(c))

					if str(responce) in numlist:
						return int(responce)
					else:

						clear()
						print(termcolor.colored("Erro digite uma opção valida !!", "red"))
						break
			else:
				clear()
				print(termcolor.colored("Erro digite um número inteiro !!!", "red"))
				break
				
	def ReadInt(self,pergunta):

				while True:
					responce = input(pergunta)
					
					if responce.isnumeric() == True:
						return int(responce)
					else:
						clear()
						print(termcolor.colored("Error Type a number"))
						break
					
#Funções de calculo do programa
	
def ShowMultipleTable():

	clear()
	while True:
		table = Table("Show Multiple Table", "=", 30)
		option = ReadOption(["Back to menu","Show a multiple table"])
		
		table.ShowTitle()
		option.ShowOptions()
		table.CloseTitle()
		
		responce = option.ReadOption("Type a option: ")
		
		if responce == 0:
			clear()
			break
		else:
			while True:
				print("If you wish exit type \"clear\" ...")
				num_tabuada = input("Type a number to show a multiple table: ")
				
				if num_tabuada.isnumeric() == False:
					if num_tabuada == "clear":
						clear()
					elif num_tabuada == "exit":
						break
					else:
						print(termcolor.colored("Error Type a integer number", "red"))
						
				else:
					for c in range(0,10):
						print(f"{num_tabuada} X {c} = {int(num_tabuada) * c}")
		
def PracticeMultipleTable():
	pass
				
def LearnMultipleTable():
	while True:
		

while True:

	table = Table("Multiple Table", "=", 30)
	
	option = ReadOption(["Exit program","Show Multiple Table", "Practice Multiple Table", "Learn Multiple Table"])
	
	table.ShowTitle()
	option.ShowOptions()
	
	table.CloseTitle()
	
	res = option.ReadOption("Type a option: ")
	
	if res == 0:
		break
	if res == 1:
		ShowMultipleTable()
