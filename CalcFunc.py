class CalcFunctions:
	def __init__(self):
		pass
	def additions(self,numberOfNumbers1):
		self.add=0
		for i in range(0,numberOfNumbers1,1):
			self.add+=(int(raw_input("Enter the one of the numbers you want to add\n> ")))
		print("Your result is {}!".format(self.add))

	def subtraction(self,subtractee,subtracter):
		result=subtractee-subtracter
		print("Your result is {}!".format(result))
		



	def multiplication(self,numberOfNumbers2):
		mult=1
		for i in range(0,numberOfNumbers2,1):
			if(i==0):
				num=float(raw_input("Enter the number you want to multiply.\n>"))
			else:
				num=float(raw_input("Enter another number to multiply.\n> "))
			mult*=num
		print("Your total is {}.".format(mult))

	def division(self,dividee,divider):
		resulto=dividee/divider
		print("Your total is {:.2f}".format(resulto))
		

