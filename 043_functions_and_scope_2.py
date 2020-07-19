# variables that are deficed outside any fucntion are global and they can be used anywhere
def myFunction():
    print("Do I know that variable?", var)
    
var = 1
myFunction()
print(var)

# Let's see this example:

def print_number():
    print("the number is", number)
    number = 45 # once you asign a value to a variable in a function, it becomes a variable that is local to the function
                # if there is a variable with the same name globally the function will ignore it
                # This code cause an error because the function do not know about the variable in line 17
    
number = 4
print_number()
print(number)