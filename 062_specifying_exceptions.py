# We would like to be specific and have an specific code for each exception:
# Python allows us to branch the exceptions:
#     try:
#         # code code ...
#     except nameOfTheException1:
#          # code for exception 1
#     except nameOfTheException2:
#          # code for exception 2
#       .
#       .
#       .
#     except nameOfTheExceptionX:
#          # code for exception X
#     except:
#          # last resort
# Python provides some keywords to handle exceptions, properly: try and except

try: # try menas "execute this and if something happens go directly to the except"
    firstNumber = int(input("First number: "))
    secondNumber = int(input("Second number: "))
    division = firstNumber / secondNumber
    print(division)
except ValueError:
    print("\n OOPS! that's not an integer number")
except ZeroDivisionError:
    print("\n Opps we can NOT dived by 0 that's not ok in math")
except KeyboardInterrupt:
    print("\n OK Ok I got you, you have to leave, bye bye")
# note that a final general except (unnamed branch/not dedicaded exception)
# is not mandatory but in some cases you don't know all of the possible exceptions,
# so you may want to use it and say "Oops! something happes"

# Expect an exception to be raised if you are not handling it