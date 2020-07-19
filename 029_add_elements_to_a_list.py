# We can use the .append() method to add elemets to an existing list:
print("-------USING THE .append() METHOD--------")
my_list = [1,2,3,4,5,6]
print("Original list:", my_list)
my_list.append(1000)
print("After adding the number 1000:", my_list)

# we can use a for loop and the range function to add multiple items:
num = 1001
for i in range(9): # remember range(number) means 0 to number-1
    my_list.append(num)
    num += 1

print(my_list)

print("-------USING THE .insert() METHOD--------")
# the isert method allows us to insert a new item in a specific index
# the rest of the items are moved one idex
print("List to use:", my_list)
print("index [3] =", my_list[3])
my_list.insert(3, 0)
print("After inserting the number 0 in index 3:", my_list)

print("Doing some more cool stuff:")
myList = [] # creating an empty list

for i in range(5):
    myList.insert(0, i + 1)

print(myList)