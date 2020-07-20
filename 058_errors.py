import math

x = float(input("Enter x: ")) # there is no guarantee that the string can be converted into a float value 
# Enter x: abracadabra      -> ValueError: could not convert string to float: 'abracadabra'

y = math.sqrt(x) # sqrt() function fails if it gets a negative argument.
# Enter x: -4
#  y = math.sqrt(x) # sqrt() function fails if it gets a negative argument.
# ValueError: math domain error

print("The square root of", x, "equals to", y)