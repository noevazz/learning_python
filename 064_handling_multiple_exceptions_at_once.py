"""
If you want to handle two or more exceptions in the same way, you can use the following syntax:
try:
    :
except (exc1, exc2):
    :

"""

# Option 1
def badFUn(n1, n2):
    return n1/n2

try:
    badFUn(1, 0)
except (ZeroDivisionError, ValueError):
    print("Opps!")

# Option 2
def badFun_2(n1, n2):
    try:
        return n1/n2
    except (ZeroDivisionError, TypeError): # about TypeError-> TypeError: unsupported operand type(s) for /: 'str' and 'int'
        print("oh man, you did it again!")

badFun_2(1,0)
badFun_2("not a number",0)