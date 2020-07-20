# Let's take a look at two common exceptions (comments one of them to review the other)

print("-------------- ZeroDivisionError --------------")
firstNumber = int(input("First number: "))
secondNumber = int(input("Second number: "))
print(firstNumber / secondNumber) # THERE'S a possible exception here:
# if the second number is 0 a ZeroDivisionError exception will be raised

# with the only knowledge we have at this moment we can do the following to
# avoid the program to raise the exception and exit (of course you will need to commend line 7)
if secondNumber != 0:
    print(firstNumber / secondNumber)
else:
    print("This operation cannot be done.")
# Of course there's another issue if you provide a number that int() cannot convert into integer (ValueError:)



print("-------------- IndexError --------------")
list = []
# If you try to acces an index that does NOT exist this will raise and exception
#x = list[0] # index 0 does NOT exists, IndexError exception will be raised

# Using the knowledge we have at this point (of course: comment line 22):
test_index = 0
x = 0
if test_index < len(list) and len(list)>0:
    x = list[test_index]
    print(x)
else:
    print("That index does not exists")