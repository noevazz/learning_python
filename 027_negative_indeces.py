# Negative indexes are legal

my_list = [4, 7, 10, 6]
print("List=", my_list)

# An element with an index equal to -1 is the last one in the list
print("[-1] index=", my_list[-1])

# The element with an index equal to -2 is the one before last in the list
print("[-2] index=", my_list[-2])

# We can also use the "del" insttruction to delete an element
print("List before deleting the [-2] index=", my_list)
del my_list[-2]
print("List after deleting the [-2] index=", my_list)