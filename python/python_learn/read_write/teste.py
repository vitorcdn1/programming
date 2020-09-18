def Content():
	arquivo = open("teste.txt", "r+")

	content = arquivo.readlines()
	arquivo.close()

	return content

def WriteSomething(palavra):


	arquivo = open("teste.txt", "r+")
	arquivo.writelines(content)
	arquivo.close()

arquivo = open("teste.txt", "r+")
arquivo.write("teste\n")
arquivo.close()

print(Content())
