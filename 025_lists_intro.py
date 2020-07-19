print('A lists is a collection of elements, but each element is a scalar.')
print("example: my_list = [2, 4, 5, 293, 31, 0, 7]")
my_list = [2, 4, 5, 293, 31, 0, 7]
print("execution:", my_list)

print("\nYou can access a specific element by its index (index start at 0 so the first element has the index 0):")
print("first element:", my_list[0])

print("To know the length of list use the len(list) function")
print("len(my_list)=", len(my_list))

# we can check is a value is inside a list:
print("checking if a value is inside a list:", 3 in my_list)
print("checking if a value is not inside a list:", 3 not in my_list)