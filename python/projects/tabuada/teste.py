
class Table:
	def __init__(self, name, letra, num):
		self.name = name
		self.letra = letra
		self.num = num

	def ShowTitle(self):
		print(self.letra*self.num)

	def CloseTitle(self):
		result = (2 + len(self.name)) + (self.num * 2)
		print(self.letra*result)
		
		
		
		
teste = Table("Multiple Table","=", 30)

teste.ShowTitle()

teste.CloseTitle()
