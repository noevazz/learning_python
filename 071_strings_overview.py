# len() function used for strings returns a number of characters contained by the arguments.
print("----- the len function -----")
word = 'by'
print(len(word))

empty = ''
print(len(empty))

i_am = 'I\'m'
print(len(i_am))

# Multiline strings
print("----- Multiline strings -----")
multiLine = '''Line #1
Line #2'''
print(len(multiLine))
# expect to have +1 for each invisible \n

# concatenating strings
print("----- concatenating strings -----")
str1 = 'abc'
str2 = 'def'
print(str1 + str2)

# replicating strings
print("----- replicating strings -----")
str1 = 'hello'
print(3*str1) # same as str1 * 3 because replications is commutative
# Note: shortcut variants of the above operators are also applicable for strings (+= and *=).