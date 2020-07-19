print("Lists can contain any value, even more lists")
list_1 = [ [1,2,3], [4,5,6], [7,8,9] ]
print("list_1=", list_1)
print("it doesn't matter the item type, you cana access the item using its index:")
print("list_1[1]=", list_1[1])
print("Now we do the same to access a specific item:")
print("list_1[1][0]=", list_1[1][0])
print("list_1[1][1]=", list_1[1][1])
print("list_1[1][2]=", list_1[1][2])

print("\n if you don't know the length of each list use 'in':")
list_2 = [ [1,2,3,4,5], [6,7], [8,9,10] ]
for x in list_2:
    # x returns each list
    for y in x:
        print(x, "has", y)
    print()