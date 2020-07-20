from random import randint

class MyNiceClass():
# whenever you see "self" it is used to refer to the object. This is useful (and sometimes required)
# so each object can have its own varaible
    def __init__(self): # self is required in the constructor
        print("Hi :D") # code inside __init__() will be executed once you instance the class for each obkect
        self.number = randint(3, 9) # again, "self" it is used to refer to the object.

obj = MyNiceClass()
print(obj.number)