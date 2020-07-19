# when assigning values we have:
x = 3
y = 50
print(f"x={x}, y={y}")
# WHat if we now want to swap thos values:
x, y = y, x
print(f"x={x}, y={y}")

# The same can be done with lists:
print("----Swapping values in a list----")
my_list = [7, 3, 5, 1, 0, 8]
print(my_list)
my_list[0], my_list[-1] = my_list[-1], my_list[0] # swapping the first item (index 0) and the last item
print(my_list)
# we can make use of this feature to swap the whole list:
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)