# Slicing allows us to retrive a very specict set of items of a list
my_list = [5, 2, 1, 3, 7, 9, 10]
print("The sintax (slice notation) is my_list[start: stop: step],\n\
 ----> start, stop and step are optionals but you need to use at least one ':'")
print("We have been using 'start' all this time:")
print("    my_list[-1]=", my_list[-1])
print("Slice notation returns a new list, so you can also use this feature to copy a list and not the reference")


print("\n------- Using start and stop -------")
print("Note: stop really means stop-1 ")
print("    my_list=", my_list)

print("\nThe last 4 items are my_list[my_list.index(3): len(my_list)], let's see:")
# .index() returns the index of an item
print(my_list[my_list.index(3) : len(my_list)])

print("\nOr let's make life easier and use negative values, let's see:")
print("    my_list[-4: len(my_list)]=", my_list[-4: len(my_list)])

print("\nif you dont specify stop it means that you want the rest of the list:")
print("    my_list[-4:]=", my_list[-4:])

print("\nAnd if you don't specify the 'start' in means you to start from the first item [0]")
print("First 3 items (indeces 0, 1 and 2)= my_list[:3], let's see:") # stop = stop-1, so 3-1=2
print(my_list[:3])

print("\nGetting the whole list: my_list[:]")
print(my_list[:])

print("\nSlicing is useful to retrieve specific values and also to loop those values:")
print("changig the values for a specific subset:")
for item in my_list[-3:]: # the last 3 items
    my_list[ my_list.index(item) ] = item*10000
print(my_list)

print("\n------- Using start and stop and step -------")
print("by default step = 1, step will ignore the amout of items you want,")
my_list = [3, 5, 7, 89, 4, 0, 1]
print("my_list=", my_list)
print("my_list[::3]=", my_list[::3])
print("""EXPLANATION:
my_list =      [3,  5,  7,  89,  4,  0,  1]
                    1   2    3   1   2   3
my_list[::3]  pick          pick        pick
""")