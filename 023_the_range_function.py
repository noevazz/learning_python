# The range() function may accept up to three arguments 
# range(start, stop[, step]

# Print first 5 numbers using range function
for i in range(5):
    print(i, end=', ')

# using start, stop, and step arguments in range()
print("Printing All even numbers between 2 and 10 using range()")
for i in range(2, 10, 2):
    print(i, end=', ')


# Reverse range option 1
print ("Displaying a range of numbers by reverse order")
for i in range(5, -1, -1):
    print (i, end=', ')

# Revers range option 2
print("Printing reverse range using reversed()")
for i in reversed(range(0, 5)):
    print(i)
