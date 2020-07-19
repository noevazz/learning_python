# Python offers another convention for passing arguments,
# where the meaning of the argument is dictated by its name,
# not by its position - it's called keyword argument passing.
def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction(firstName = "James", lastName = "Bond")
introduction(lastName = "Skywalker", firstName = "Luke") # note that here the position does not matter

# Of course, you mustn't use a non-existent parameter name.
#introduction(surname="Skywalker", firstName="Luke") # error
# TypeError: introduction() got an unexpected keyword argument 'surname'

print()
# Mixing positional and keyword arguments:
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(3, c = 1, b = 2)
adding(3, b = 1, c = 2)
#adding(3, b = 1, 2) # error: SyntaxError: positional argument follows keyword argument
# IMPORTANT: always use positional arguments first, and the keyword arguments

# Also be sure to not pass one arguments more than 2 times:
adding(2, a=3, c=45) # a was already provided
# error: TypeError: adding() got multiple values for argument 'a'
