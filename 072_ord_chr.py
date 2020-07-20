print("------ ord ------")
# if you want to know a specific character's ASCII/UNICODE code point value,
# you can use a function named ord() (as in ordinal).
print(ord("A")) # 65
print(ord("a")) # 97
print(ord(" ")) # 32 (a-A)
print(ord("ę"))
# The function needs a >strong>one-character string as its argument
# breaching this requirement causes a TypeError exception,
# and returns a number representing the argument's code point.
#print(ord("sadasdasd")) # TypeError: ord() expected a character, but string of length 9 found

print("------ chr ------")
# If you know the code point (number) and want to get the corresponding character,
# you can use a function named chr().
print(chr(97))
print(chr(945))