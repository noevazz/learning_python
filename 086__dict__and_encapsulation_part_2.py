"""Python objects, when created, are gifted with a small
set of predefined properties and methods.
Each object has got them, whether you want them or not.
One of them is a variable named __dict__ (it's a dictionary)."""

class ExampleClass:
    def __init__(self, val):
        self.first = val

    def setSecond(self, val):
        self.second = val
    
    def hiden(self):
        self.__secret = 666 # note that the way python hides a variables is by changing its name (property name mangling)
        # __varName to _className__varName
        # in this case __secret to _ExampleClass__secret
        # it's just a very basic way because you can use _ExampleClass__secret to access the variable

obj1 = ExampleClass("first obj1") # we do not invoke setSecond so objq wont have that variable
obj1.hiden()
print("obj1.__dict__ =", obj1.__dict__)

obj2 = ExampleClass("first  obj2")
obj2.setSecond("second obj2")
obj2.hiden()
print("obj2.__dict__ =", obj2.__dict__)

obj3 = ExampleClass("first obj3")
obj3.setSecond("second obj3")
obj3.second = "second" # the variable is not hided (__second) so we can made changes
obj3.hiden()
print("obj3.__dict__ =", obj3.__dict__)
#print(obj3.__secret) # Error

obj4 = ExampleClass("first obj4")
obj4.second = "second obj4" # note tha we are setting a variable that do not exist so it will be create on the fly
obj4.third = "third obj4" # note tha we are setting a variable that do not exist so it will be create on the fly
obj4.__secret = 2020 # we are not accessing the variable defined in the hiden() method,
#                      we are creating and assigning a new variable on the fly (__ doesn't mean hide in this case)
#                      it is a error if you try to access obj4.__secret before this line because it does not exists
obj4.hiden()

print("obj4.__dict__ =", obj4.__dict__) 
print(obj4._ExampleClass__secret) # note that hiden() creates the _ExampleClass__secret variable and it's available