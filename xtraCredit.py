def mux_letters(string,numberOfLetters):
	newstring=""
	for letters in string:
		newCharacters=letters*numberOfLetters
		newstring+=newCharacters
	return(newstring)
lol=mux_letters("lets hug, what ryhmes with hug me?",2)
print(lol)
lmao=mux_letters("I will Find you",3)
print(lmao)