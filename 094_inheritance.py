"""
inheritance allows us to grant children (sub class) with all the features of a parent class (super class)
"""
class SuperOne:
    def hello_1(self):
        print("Hello 1")

class SuperTwo:
    def hello_2(self):
        print("Hello 2")


class Sub(SuperOne, SuperTwo): # note that a class can have more than one parent
    pass # now all objects of Sub can use the features of SuperOne and SuperTwo

# BTW: multiple inheritance violates the single responsibility principle
# (more details here: https://en.wikipedia.org/wiki/Single_responsibility_principle)
# as it makes a new class of two (or more) classes that know nothing about each other;

obj = Sub()
obj.hello_1()
obj.hello_2()
