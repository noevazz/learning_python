# Python provides some keywords to handle exceptions, properly: try and except
try: # try means "execute this and if something happens go directly to the except"
    firstNumber = int(input("First number: "))
    secondNumber = int(input("Second number: "))
    division = firstNumber / secondNumber
    print(division)
except: # code inside except is executed if an exception is raised
    print("\n OOPS! this operation cannot be done.")
    # Because our except is too general we can handle all posible exceptions:
    #  - ValueError
    #  - ZeroDivisionError
    #  - KeyboardInterrupt ( when you press Ctrl+C)