"""
The super() function accesses the superclass without needing to know its name:
"""
class SuperClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(SuperClass):
    def __init__(self, name):
        super().__init__(name) # you don't need to pass self when using super() 


obj = Sub("Andy")

print(obj)