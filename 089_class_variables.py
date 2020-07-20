# A class variable is a property which exists in just one copy and is stored OUTSIDE any object.
#   NO INSTANCE variable exists if there is no OBJECT in the class
#   a CLASS variable exists in one copy even if there are NO OBJECTSs in the class.
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1 # Note that we are calline the class

obj1 = ExampleClass()
obj2 = ExampleClass()
# The ExampleClass.counter variable does not appear in the obj.__dict__ because is a class variable
# you can do objX.counter to retrieve the value because is an instance of the class
print("obj1.__dict__ =", obj1.__dict__, "   obj1.counter=", obj1.counter)
print("obj2.__dict__ =", obj2.__dict__, "   obj2.counter=",  obj2.counter)
print(ExampleClass.counter)

print()

# if you try to change the value of a class variable from an object you will create a variable on the fly instead:
obj1.counter = 99999
print("obj1.__dict__ =", obj1.__dict__, "   obj1.counter=", obj1.counter) # now you cannot access the class variable in this way, now you are accessing the variable that you created on the fly
print("obj2.__dict__ =", obj2.__dict__, "   obj2.counter=",  obj2.counter) # we can still do it in obj2 because we did not made changes
print(ExampleClass.counter)