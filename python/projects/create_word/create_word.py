import termcolor
import os
import platform

from ReadOption import Table, ReadOption, clear, GeneratePass


clear()

alphabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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

	if responce == 1:
		clear()

		while True:

			table = Table("Generate random phrase", "=", 10)

			option = ReadOption([
				"Back to menu",
				"Generate a single password",
				"Generate more than one password",
				"Generate passwords to a file"
			])

			table.ShowTitle()

			option.ShowOption()

			table.CloseTitle()

			responce = option.ReadOption("Type a option: ")

			if responce == 0:
				clear()
				break
			if responce == 1:
				clear()
				
				siz = option.ReadOption("What's the size of the pass that you want to generate: ")
				ynl = option.ReadBool(pergunta = "Do You want lowercase in your pass: ", true = "yes", false = "no")
				ynu = option.ReadBool(pergunta = "Do You want uppercase in your pass: ", true = "yes", false = "no")
				ynn = option.ReadBool(pergunta = "Do you want number in your pass: ", true = "yes", false = "no")

				print(GeneratePass(tamanho = siz, lower = ynl, upper = ynu, num = ynn))

				pass
			if responce == 2:
				pass
			if responce == 3:
				pass
