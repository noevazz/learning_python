# in order to use our own function we first need to define them:
def my_first_function():
    print("Hello world, this is my first function")

# Now we can call (INVOCATION) our function:
my_first_function()

# remember the "pass" keyword that we saw when we were learning about loops, it can be used if you don't know what to execute:
def other():
    pass
# of course if you call this function it will not do anything:
other() # but you can do it to start laying out your program

# Now you can call you function at any time:
my_first_function()
my_first_function()
my_first_function()

# NOTE tha you defined the function to not receive any argument,
# Passing an argument will cause an error because python knows that the functions is not expecting arguments
my_first_function(23, 43, "hello") # this will cause an error
# TypeError: my_first_function() takes 0 positional arguments but 3 were given