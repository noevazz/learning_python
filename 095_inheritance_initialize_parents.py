"""
if the parent of a sub class has its constructor defined, you need to initialize the parent in the subclass
"""
class SuperOne:
#   we do not define the constructor here
    def hello_1(self):
        print("Hello 1")

class SuperTwo:
    def __init__(self, argument1): # argument but not used it
        self.a = 23

    def hello_2(self):
        print("Hello 2")

class SuperThree:
    def __init__(self, argument1): # argument used
        self.a = argument1

    def hello_3(self):
        print("Hello 3", self.a)


class Sub(SuperOne, SuperTwo, SuperThree):
    def __init__(self):
        SuperThree.__init__(self, ":D") # only SuperThree is using the arguments of its constructor
#                                         so I need to initialize it
#                                         otherwise:
#           TypeError: __init__() missing 1 required positional argument: 'argument1'

obj = Sub()
obj.hello_1()
obj.hello_2()
obj.hello_3()
