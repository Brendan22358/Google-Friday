import math
from __future__ import print_function
def addition_simple(x,b):
	addition=x+b
	return(addition)
def subtratciont_simple(x,b):
	subtraction=x-b
	return(subtraction)
def multiplication_simple(x,b):
	multiplication=x*b
	return(multiplication)
type=raw_input("Enter what type of math you want to do:\n>")
if(type=="addition"):
	addition_simple(a,b)
	print(addition)
if(type=="subtraction"):
	subtraction_simple(a,b)
	print(subtraction)
if(type=="multiplication"):
	multiplication_simple(a,b)
	print(multiplication)
