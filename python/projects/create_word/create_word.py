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

			table = Table("Generate rando phrase", "=", 10)

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
				print(GeneratePass())
				pass
			if responce == 2:
				pass
			if responce == 3:
				pass