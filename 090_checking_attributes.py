# Python provides a function which is able to safely check if any object/class contains a specified property. 
# use hasattr(class/object, "attribute to check") to check

# do not get confused, hasattr does not search in __dict__

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.first = val
        ExampleClass.counter += 1

obj1 = ExampleClass()
print(hasattr(obj1, "counter"))
print(hasattr(ExampleClass, "counter"))
print(hasattr(obj1, "first"))
print(hasattr(ExampleClass, "first")) # "fisrt" is an object varaible
