"""
The raise instruction may also be utilized with the absence of the exception's name
    !!! There is one serious restriction:
    this kind of raise instruction may be used inside the except branch only;
    using it in any other context causes an error-> RuntimeError: No active exception to reraise
"""

def badFun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise # only use an unnamed raise inside an except block

try:
    badFun(0)
except ArithmeticError:
    print("I see!")