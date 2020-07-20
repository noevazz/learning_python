# __module__ is a string, it stores the name of the module which contains the definition of the class.
# in this case the name of this module (__name__) is "__main__"
class Classy:
    pass

print(Classy.__module__)
obj = Classy()
print(obj.__module__)