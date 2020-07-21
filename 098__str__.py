"""
When Python needs any class/object to be presented as a string
(putting an object as an argument in the print() function invocation fits this condition) it tries to invoke a method named __str__() from the object and to use the string it returns.
"""
class Default():
    pass


class Star:
    def __str__(self):
        return "Hi I'm a Start"


d = Default()
s = Star()

print(d)
print(s)