# functions cause some effect, sometimes based in the data you provide

# the print() function receive 0 or more data (arguments) and then prints the arguments to the standard output (console)
print(24) # you can numbers, (without decimal part are called int or integers)
print(100.3) # you can print numbers with decimals (float numbers)
print("you can print strings") # strings are a set of characters
print('strings can also be defined using single quotes')
print("use comas to separate the arguments", 2020, "hello", "bye", -23, 10)
# By default print() separates each argument with a space and also it prints a new line at the end
# you can chage its default behavior:
print("using", "two", "dashes", "instead", "of", "one", "space", sep="--")
# the ´sep´ argument (separation) needs to be placed at the end
print("you can also change the end, in this case we added 3 new lines", end="\n\n\n")
print("\\n means new line, it is called scape sequence")
# escape sequences start with a backslash
# \\ is another escape sequence, it let us to print a back slash
# so we can see \n in the console instead of a new line
print("you can", "use sep and end", "in the same print function", sep="-SEPARATOR-", end="-END-")
# since the end is not a new line, if you use another print its output will be next to the print above
print("hi this another print")
# finally, by default and without arguments, print() prints a new line,
# let's print 3 new lines:
print()
print()
print()


# print() is a built-in function, it means that Python already knows about it
# if you want to create your own function it needs to be defined and created in your code
