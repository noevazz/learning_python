#A list comprehension is actually a list, but created on-the-fly during program execution,
# and is not described statically.

# sintax = [ value for value in expression1 if expression2]
# it will generate a list with the values if the optional expression is True
my_list = [number for number in range(1, 11)] # this will create a list with al the numbers generated
print(my_list)
even_numbers = [number for number in range(1, 11) if number%2==0] # this will create a list with al the numbers generated
print(even_numbers)

print("\n complicationg the things")
print("creating lists in list using comprehension lists")

a = [[i*2 for i in range(5, 11)] for a in range(3)]

print(a)