#!/usr/bin/env python3 
""" 
The line starting with #! has many names - it may be called shabang, shebang, hashbang, poundbang or
even hashpling (don't ask us why). The name itself means nothing here - its role is more important.
From Python's point of view, it's just a comment as it starts with #. For Unix and Unix-like OSs (including MacOS)
such a line instructs the OS how to execute the contents of the file (in other words, what program needs to be launched to interpret the text).
In some environments (especially those connected with web servers) the absence of that line will cause trouble;
"""

__counter = 0
"""
Python has no means of allowing you to hide such variables from the eyes of the module's users.
You can only inform your users that this is your variable, that they may read it, but that they should not modify it under any circumstances.

This is done by preceding the variable's name with _ (one underscore) or __ (two underscores), but remember, it's only a convention.
Your module's users may obey it or they may not.
"""

def suml(list):
	global __counter
	__counter += 1
	sum = 0
	for el in list:
		sum += el
	return sum

def prodl(list):
	global __counter	
	__counter += 1
	prod = 1
	for el in list:
		prod *= el
	return prod

if __name__ == "__main__":
	print("I prefer to be a module, but I can do some tests for you")
	l = [i+1 for i in range(5)]
	print(suml(l) == 15)
	print(prodl(l) == 120)