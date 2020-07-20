print("\n----- min function ------")
# finds the minimum element of the sequence passed as an argument.
# There is one condition - the sequence (string, list, it doesn't matter)
# cannot be empty, or else you'll get a ValueError exception.
string = 'The Knights Who Say "Ni!"'
print('[' + min(string) + ']') # note it print the space character
lst = [0, 1, 2]
print(min(lst))

print("\n----- max function ------")
#  finds the maximum element of the sequence.
string = 'The Knights Who Say "Ni!"'
print('[' + max(string) + ']')
lst = [0, 1, 2]
print(max(lst))

print("\n----- list function ------")
# The list() function takes its argument (a string) and creates a new list containing all
#    the string's characters, one per list element.
# Note: it's not strictly a string function - list() is able to create a new list from many
#    other entities (e.g., from tuples and dictionaries).
print(list("abcabc"))