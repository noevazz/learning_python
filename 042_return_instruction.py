# the return instructions allows is to return a value in a function

def adding(a, b, c):
    return a+b+c

# you can save the value of that return on a variable, use it as an argument, etc.
print(adding(1,2,4)) # Here I am using the return value as an argument to the print function

result = adding(2,5,1) # or I can save the value

adding(4,0,1) # but that is not mandatory it just means that no entiti wil handle the return value

# IMPORTANT_ whenever a functions reach the return instruction it will return the value and the exit the function execution (you can have more than one return)

def odd_or_even(number):
    if number%2 == 0:
        return "even"
    else:
        return "odd"

print(odd_or_even(10))

# you can define a value to be returned but this is not mandatory:
def bye():
    print("bye")
    return # noe we are not returning any value
    print(":D") # this line will be ignored because line above exits the function

bye()
# by default functions with no return instruction (and also functions with only return) return None:
print(bye())
def no_return():
    pass
print(no_return())
