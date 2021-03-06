from random import randint

class MyNiceClass():
# whenever you see "self" it is used to refer to the object. This is useful (and sometimes required)
# so each object can have its own varaible
    def __init__(self): # self is required in the constructor
        print("Hi :D") # code inside __init__() will be executed once you instance the class for each obkect
        self.number = randint(3, 9)
    
    def give_me_a_number(self, a=0, b=10): # it's a function so you already know how to use them
        # when calling this function do not worry about self, python pass the object for you
        return randint(a, b)
    # the "self" is required in classes' methods, the name is not required to be self, but is a convention


obj = MyNiceClass()
print(obj.number)
print(obj.give_me_a_number(b=5))