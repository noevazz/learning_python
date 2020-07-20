print("\n----- capitalize ------")
# - If the first character inside the string is a letter
#   (note: the first character is an element with an index equal to 0, not just the first visible character),
#   it will be converted to upper-case;
# - All remaining letters from the string will be converted to lower-case.
print(1, "Alpha".capitalize())
print(2, 'ALPHA'.capitalize())
print(3, ' Alpha'.capitalize())
print(4, '123'.capitalize())
print(5, "αβγδ".capitalize())




print("\n----- center ------")
# makes a copy of the original string, trying to center it inside a field of a specified width.
print(1, '[' + 'Beta'.center(2) + ']')
print(2, '[' + 'Beta'.center(4) + ']')
print(3, '[' + 'Beta'.center(10) + ']')
print(4, '[' + 'Beta'.center(2, "*") + ']')
print(5, '[' + 'Beta'.center(4, "*") + ']')
print(6, '[' + 'Beta'.center(10, "*") + ']')




print("\n----- startswith ------")
# checks if a given string starts with the specified substring.
print("omega".startswith("meg"))
print("omega".startswith("om"))




print("\n----- endswith ------")
# checks if the given string ends with the specified argument and returns True or False
t = "zeta"
print(1, t.endswith("a"))
print(2, t.endswith("A"))
print(3, t.endswith("et"))
print(4, t.endswith("eta"))




print("\n----- index method ------")
#  searches the sequence from the beginning, in order to find the first element of the value specified in its argument.
# Note: the element searched for must occur in the sequence - its absence will cause a ValueError exception.
print(1, "aAbByYzZaA".index("b"))
print(2, "aAbByYzZaA".index("Z"))
print(3, "aAbByYzZaA".index("A"))




print("\n----- find ------")
# it finds the first occurrence of the specified value.
# returns -1 if the value is not found.
txt = "Hello, welcome to my world."
print(1, txt.find("welcome"))
print(2, txt.find("not in the string"))




print("\n----- rfind ------")
# The one-, two-, and three-parameter methods named rfind() do nearly the same things as their counterparts
# (the ones devoid of the r prefix), but start their searches from the end of the string, not the beginning
# (hence the prefix r, for right).
# string.rfind(value, start, end) 
print(1, "tau tau tau".rfind("ta"))
print(2, "tau tau tau".rfind("ta", 9)) # returns -1 if the value is not found.
print(3, "tau tau tau".rfind("ta", 3, 9))




print("\n----- count ------")
# counts all occurrences of the element inside the sequence.
# The absence of such elements doesn't cause any problems.
print(1, "abcabc".count("b"))
print(2, 'abcabc'.count("d"))




print("\n----- isalnum ------")
# checks if the string contains only digits or alphabetical characters (letters),
# and returns True or False according to the result.
print(1, 'lambda30'.isalnum())
print(2, 'ΑβΓδ'.isalnum())
print(3, '30'.isalnum())
print(4, '@'.isalnum())
print(5, 'lambda_30'.isalnum())
print(6, ''.isalnum())




print("\n----- isalpha ------")
# checks if the string contains only alphabetical characters
print(1, "Moooo".isalpha())
print(2, 'Mu40'.isalpha())




print("\n----- isdigit ------")
# checks if the string contains only digits
print(1, '2018'.isdigit())
print(2, "Year2019".isdigit())




print("\n----- islower ------")
# it is a fussy variant of isalpha() - it accepts lower-case letters only.
print(1, "Moooo".islower())
print(2, 'moooo'.islower())




print("\n----- isspace ------")
# identifies whitespaces only
print(1, ' \n '.isspace())
print(2, " ".isspace())
print(3, "mooo mooo mooo".isspace())




print("\n----- isupper ------")
# is the upper-case version of islower() - it concentrates on upper-case letters only.
print(1, "Moooo".isupper())
print(2, 'moooo'.isupper())
print(3, 'MOOOO'.isupper())




print("\n----- join ------")
# - It expects one argument as a list.
#   it must be assured that all the list's elements are strings
#   the method will raise a TypeError exception otherwise; 
# - All the list's elements will be joined into one string
#   the string from which the method has been invoked is used as a separator
# - The newly created string is returned as a result.
print(1, ",".join(["omicron", "pi", "rho"]))
print(2, "        ".join(["omicron", "pi", "rho"]))
print(3, "----".join(["omicron", "pi", "rho"]))




print("\n----- upper ------")
# makes a copy of the source string, replaces all lower-case letters with their upper-case counterparts,
# and returns the string as the result
print("I know that I know nothing. Part 2.".upper())




print("\n----- lower ------")
# makes a copy of a source string, replaces all upper-case letters with their
# lower-case counterparts, and returns the string as the result.
print(1, "SiGmA=60".lower())




print("\n----- strip ------")
#  it makes a new string lacking all the leading and trailing whitespaces.
print(1, "[" + "   aleph   ".strip() + "]")




print("\n----- lstrip ------")
# returns a newly created string formed from the original one by removing
# all LEADING whitespace or all characters enlisted in its argument.
print(1, "[" + "      tau       ".lstrip() + "]")
print(2, "pythoninstitute.org".lstrip("py"))
print(3, "www.cisco.com".lstrip("wm")) # note that m is not removed because is not a leading characte, lol




print("\n----- rstrip ------")
# Two variants of the rstrip() method do nearly the same as lstrips, but affect the opposite side of the string.
print(1, "[" + "      tau       ".rstrip() + "]")
print(2, "pythoninstitute.org".rstrip("py"))
print(3, "www.cisco.com".rstrip("wm"))



print("\n----- replace ------")
# The two-parameter replace() method returns a copy of the original string in which ALL
# occurrences of the first argument have been replaced by the second argument.
print(1, "www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print(2, "This is it!".replace("is", "are"))
print(3, "Apple juice".replace("juice", ""))
# The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.
print(4, "This is it!".replace("is", "OOOO", 1))
print(5, "This is it!".replace("is", "OOOO", 2))




print("\n----- split ------")
# it splits the string and builds a list of all detected substrings.
# The method assumes that the substrings are delimited by whitespaces
#   the spaces don't take part in the operation, and aren't copied into the resulting list.
# If the string is empty, the resulting list is empty too.
print("phi       chi\npsi   hello ".split())





print("\n----- title ------")
# it changes every word's first letter to upper-case, turning all other ones to lower-case.
print("I know that I know nothing. Part 1.".title())






# Python strings have a significant number of methods intended exclusively for processing characters.
# Don't expect them to work with any other collections.
# The complete list of is presented here: https://docs.python.org/3.4/library/stdtypes.html#string-methods.