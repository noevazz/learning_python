# Python's strings are sequences. It's time to show you what that actually means.
# Strings aren't lists, but you can treat them like lists in many particular cases.


print("----- Indexing strings ------")
exampleString = 'silly walks'
print(exampleString[2])
print(exampleString[-1])

print("\n----- iterating strings ------")
for ix in range(len(exampleString)):
    print(exampleString[ix], end='   ')

print("\n----- slice strings ------")
alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

print("\n----- in and not in operators ------")
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

# !!!!!!!Python strings are immutable!!!!!!!
print("\n----- Python strings are immutable ------")
alphabet = "abcdefghijklmnopqrstuvwxyz"
del alphabet[0] # exception
alphabet.append("A") # exception
alphabet.insert(0, "A") # exception

# DO NOT confuse immutable with concatenation:
# comment the errors above to see the following code
alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "A" + alphabet
alphabet = alphabet + "A"
print(alphabet)