"""
__bases__ is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.

!!!!! only classes have this attribute - OBJECTS DO NOT !!!!!

but if we have a class we can use __name__ to get its name as a string
"""
class SuperOne:
    def hello_1(self):
        print("Hello 1")

class SuperTwo:
    def __init__(self, argument1):
        self.a = 23

    def hello_2(self):
        print("Hello 2")

class SuperThree:
    def __init__(self, argument1):
        self.a = argument1

    def hello_3(self):
        print("Hello 3", self.a)

class Sub(SuperOne, SuperTwo, SuperThree):
    def __init__(self):
        SuperThree.__init__(self, ":D") 

obj = Sub()
obj.hello_1()
obj.hello_2()
obj.hello_3()

print(SuperThree.__bases__)
print(Sub.__bases__)
for class_in_Sub in Sub.__bases__:
    print(class_in_Sub.__name__) # just to get the name as a string