# it kinda looks like a function, isn't it?
class MyFirstClass():
    pass

MyFirstObject = MyFirstClass()
# it does not do anything but that's your first class

# adding complexity
# classes have methods (basically they are functions)
class MySecondClass():
    def say_hi(self): # do not worry about "self" we are going to be deeper in this later
        print("Hello World")

MySecondObject = MySecondClass()
MySecondObject.say_hi() # now we can use the methods, sintax->  object_name.method_name()
#                         this is called dotted notation                             
# it does not do anything but that's your first class