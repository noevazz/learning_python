# Any of the list's elements may be removed at any time - this is done with an instruction named del (delete).
# Note: it's an instruction, not a function.

print("\n--------- using del instruction to delete an item ---------")
numbers = [10, 3, 34, 6, 8, 0, 81]
print(numbers)
print("After deleting index [1]=", numbers[1])
del numbers[1]
print(numbers)

print("----")
print("Now I will be deleting the last element:")
# if the index starts at 0 it meand tje last elements is (number of elements)-1
print("List before deleting that item=", numbers)
del numbers[len(numbers)-1]
print("after deleting the last item=", numbers)

print("\n--------- using .pop() to delete an item ---------")
# the pop method delete an item by specifying its index,
# ALSO the pop method return the deleted item
fruits = ['apple', 'banana', 'cherry']
print(f"The item '{fruits.pop(1)}' will be deleted:")
print(fruits)

print("\n--------- using .clear() to clear a list ---------")
# we can clear a list and have [] (and empty list)
short_list = [1,2]
print("Before using the clear method:")
print(short_list)
short_list.clear()
print("after using the clear method:")
print(short_list)

print("\n--------- Deleting the whole list ---------")
# We can delete the entire list:
del numbers
print(numbers) # Note this will cause an error because the "number" list no longer exists
# NameError: name 'numbers' is not defined

