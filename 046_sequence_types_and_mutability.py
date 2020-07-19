# A sequence type is a type of data in Python which is able to store
# more than one value (or less than one, as a sequence may be empty),
# and these values can be sequentially (hence the name) browsed, element by element.

# Lists are sequences

# As the for loop is a tool especially designed to iterate through sequences,
# we can express the definition as: a sequence is data which can be scanned by the for loop.

# mutability - is a property of any of Python's data that describes its readiness to be freely
# changed during program execution. There are two kinds of Python data: mutable and immutable.

# Lists are mutable since you are allowed to modify wach single item
# Strings are also sequences but they are immutable:
name = "noe vazquez"
print(name[1])
del name[1] # error, you cannot modify a single item in an immutable sequence