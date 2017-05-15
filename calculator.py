from CalcFunc import CalcFunctions
add=CalcFunctions()
sub=CalcFunctions()
div=CalcFunctions()
mult=CalcFunctions()
type1=raw_input("What type of math would you like to do? Type 1 for addition, 2 for subtraction,\n3 for division, 4 for multiplication or 5 to close the program\n> ")
while(type1!="5"):
	if(type1=="1"):
		numbers=int(raw_input("How many numbers do you want to add?\n>"))
		add.additions(numbers)
	if(type1=="2"):
		subtract1=float(raw_input("Enter your subtractee. (What you want to subtract from)\n> "))
		subtract2=float(raw_input("Enter your subtracter. (What you are going to subtract)\n> "))
		sub.subtraction(subtract1,subtract2)
	if(type1=="3"):
		dividee=float(raw_input("Enter your dividee. (The number you are going to be dividing from)\n> "))
		divider=float(raw_input("Enter your divider. (The number you will be dividing with)\n> "))
		div.division(dividee,divider)
	if(type1=="4"):
		numofnumbs=int(raw_input("Enter the number of numbers you would like to multiply. You must multiply at least two numbers!\n> "))
		while(numofnumbs<2):
			numofnumbs=int(raw_input("Enter the number of numbers you would like to multiply. You must multiply at least two numbers!\n> "))
		mult.multiplication(numofnumbs)
	type1=raw_input("What type of math would you like to do? Type 1 for addition, 2 for subtraction,\n3 for division, 4 for multiplication or 5 to close the program\n> ")
