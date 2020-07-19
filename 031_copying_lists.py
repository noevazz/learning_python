# You cannot copy a list simply by typing list2 = list1,
# because: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.
list1 = [4,6,1]
list2 = list1
print("List1=", list1)
print("List2=", list2)
list2[0] = 100
print("After changing [0] in the second list to 100:")
print("List1=", list1)
print("List2=", list2)

# Instead use the copy METHOD:
print("\n---------Using the copy method---------")
l1 = [4,6,1]
l2 = l1.copy()
print("L1=", l1)
print("L2=", l2)
l2[0] = 100
print("After changing [0] in the second list to 100:")
print("L1=", l1)
print("L2=", l2)

# We can also use the list FUNCTION:
print("\n---------Using the list function---------")
l1 = [4,6,1]
l2 = list(l1)
print("L1=", l1)
print("L2=", l2)
l2[0] = 100

print("After changing [0] in the second list to 100:")
print("L1=", l1)
print("L2=", l2)
# a list [] is a sequence, there are other sequences,
# the list() function take a sequence an returns a list
# So we can use it with a list and it wil return a new list with the same values

