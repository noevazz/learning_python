# the input() function reads data from the standard input (your keyboard) and it returns the data as one string

name = input()
age = input("age: ") # the string inside the parenthesis is only to say something, it will no be part of the resulting string
# NOTE that even if you provide a number input() will convert it to a string
print(name, type(name),age,  type(age)) # the type() function returns the type of variable (string, int, etc.)

# if you want an integer you can convert the resulting string into a int (or float):
number = int(input("write a number: ")) # int() will try to convert the string into a number, it will raise an error if it is not possible
print(number, type(number)) 
# if everything works now you can do math with the variable
