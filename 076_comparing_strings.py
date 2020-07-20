"""
Python's strings can be compared using the same set of operators which are in use in relation to numbers.
    ==
    !=
    >
    >=
    <
    <=

There is one "but" - the results of such comparisons may sometimes be a bit surprising,
Python just compares code point values, character by character.
"""


print(1, 'alpha' == 'alpha')
# The final relation between strings is determined by comparing the first different character in both strings
# keep ASCII/UNICODE code points in mind at all times:
print(2, 'alpha' != 'Alpha')

# When you compare two strings of different lengths and the shorter one is identical to the longer one's beginning,
# the longer string is considered greater:
print(3, 'alpha' < 'alphabet')

# if the length is different the compartion is one character vs one character
print(4, 'alpha' < 'aaaaaaaaaa') # l code point is greater than a

# when length is different always take in mind the code point:
print(5, '10' == '010')
print(6, '10' > '010')
print(7, '10' > '8')
print(8, '20' < '8')
print(9, '20' < '80')

# Comparing strings with numbers:
# The only comparisons you can perform with impunity are these symbolized by the == and != operators.
# The former always gives False, while the latter always produces True.

# Using any of the remaining comparison operators will raise a TypeError exception.
print('10' == 10)
print('10' != 10)
print('10' == 1)
print('10' != 1)
print('10' > 10) # TypeError: '>' not supported between instances of 'str' and 'int'