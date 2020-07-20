"""
ABOUT self
    It identifies the object for which the method is invoked.
    You need to use it in al methods definitions of a class,
    When invoking a method, Python passes the object for you, you just need to be sure to define the method properly

    Use self inside a class whenever you want to:
        create OR CALL a instance varaible
        create (argument) or call a method inside the class (see this in the code below)
"""
class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()

obj = Classy()
obj.method()