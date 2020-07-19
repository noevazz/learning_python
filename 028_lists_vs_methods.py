#A method is a specific kind of function - it behaves like a function and looks like a function,
# IMPORTANT: but differs in the way in which it acts, and in its invocation style.

# A function is owned by the whole code, we can use it the whole program 
my_list = [1,2,3,4,5,6,7]
print(len(my_list)) # len() is a function we can used to any list
# functions looks like this: funcName(arguments)
print("print() is a function")

# A method is owned by the data it works for
my_list.sort()
# The .sort() method sorts the list ascending by default.
print("using the .sort() method=", my_list)
# A method looks like this: data.methodName(optionalArguments)

# the sorted() "function" takes a lists as argument and returns a sorted list BUT DOES NOT MODIFY THE LIST PROVIDED:
list_2 = [5, 3, 7, 0, 2]
print(sorted(list_2))
print(list_2) # sorted() does NOT modify the list passed as argument