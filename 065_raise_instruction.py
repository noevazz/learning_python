# The raise instruction raises the specified exception as if it was raised in a normal (natural) way:
# raise nameOfTheException

def badFun():
    raise ZeroDivisionError

try:
    badFun()
except ArithmeticError:
    print("OOPS!!!")