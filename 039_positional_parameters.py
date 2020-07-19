def my_function(name, age):
    print(f"Hi {name}, wow! you are {age} years old")

# the definition of the arguments in the function are positional,
# it means that when you invoke the function, the first value after the parentesis
# will be taked by the name arguments, and the second value will be taked by the age argument:

my_function("noe", 24) # expected
my_function(23, "andy") # stills works but this is not what we want, make sure to pass the arguments in its right position:
my_function("andy", 23)