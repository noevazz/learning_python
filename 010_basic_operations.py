# +, -, *, /, //, %, **
print("BINARY operators require 2 parts, e.g. 3+2:")
print("addition", 23+20)
print("addition", 23+20.) # if at least one number is float the result will be a float
print("subtraction", 1.-23)
print("multiplication", 2*9)
print("division", 5/2)
print("floor division", 5//2) # floor division (IT DOES NOOOT MEAN AN INTEGER DIVISION, see below)
print("floor division", 5.//2)
print("floor division", 5//2.)
print("mod", 10%4) #it return the remainder of the division
print("exponentiation", 2**4) # it means 2*2*2*2

print("\nUnary operators require only one part:")
print(-2)
print(+3) # well this is not really useful, numbers are positive by default
