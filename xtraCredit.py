def mux_letters(inputstring,numberoftimes):
	newstring=""
	for letters in inputstring:
		newCharacters=letters*numberoftimes
		newstring+=newCharacters
	return(newstring)
lol=mux_letters("The",2)
print(lol)
lmao=mux_letters("AAbb",4)
print(lmao)
gfus=mux_letters("Hi-There",3)
print(gfus)