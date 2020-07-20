"""
getattr() function gets the current value of an attribute, it takes two arguments:
    - An object, and its property name (as a string), and returns the current attribute's value;

isinstance() function checks the type if given value is an X type 
"""

class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.i = 3
        self.ireal = 3.5
        self.integer = 4
        self.z = 5

obj = MyClass()
print(getattr(obj, "ireal"))
print(isinstance(obj, MyClass))
print(isinstance(getattr(obj, "ireal"), float))



# Complicating the things:

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)