"""
This module has it's own __name__ variable
its default value is "__main__" only if you execute directly this program.
if you call __name__ from a different module, its name is equal to the file (without .py) of the file that contains that module

Only Objects have this variable and it returns the name of the class (in both cases)
"""

class Classy:
    pass

print(Classy.__name__)
obj = Classy()
#print(obj.__name__) # Error
