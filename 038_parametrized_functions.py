# You can pass argumets to a function, but you need to define that function to do so:

def my_function(name, age):
    print(f"Hi {name}, wow! you are {age} years old")

my_function("noe", 24)
# you can pass variables:
name = "andy"
age = 23
my_function(name, age)
# Note that is legal to have a variable named the same as a function's parameter.
#   A situation like this activates a mechanism called shadowing:
#   IMPORTANT: when using LITERALS, you are only passing the value, the modifications inside the function
#              does NOT affect the variables outside, 
#              in the other hand, passing a reference (list) it will reflect the changes in the variable inside and outside the function

# of course if you do NOT pass all the required arguments it will RAISE an error:
print()
my_function("noe")
# Parametrized functions

# You are NOT forced to use the arguments inside the function (but it will be good to do it otherwise it has no sense to define it lol)
# but you are forced to pass required arguments whenever you call a function that was defined to receive arguments.
# btw you can do whatever you want inside the function, not only print text