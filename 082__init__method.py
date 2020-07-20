# classes have an implicit method (that you can customize) to initialize your class with some values or etc.
# the __init__ method is called constructor

# __init__ cannot return a value!!!!!!!! as it is designed to return a newly created object and nothing else;

class MyNiceClass():
# whenever you see "self" it is used to refer to the object. This is useful (and sometimes required)
# so each object can have its own varaible
    def __init__(self, argument1): # self is required in the constructor.
        # argumentXs are optionals in the __init__ definition but required on instancing if you define a __init__ with arguments
        print("Hi :D") # code inside __init__() will be executed once you instance the class for each obkect

obj = MyNiceClass("here you go, here is your now required argument")