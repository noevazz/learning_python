# Dictionaries are NOT sequences, but can be easily adapted to sequence processing
# Dictionaries are mutable collections
# dictionaries are composed by keys and values:
dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

# you can access the name of a particular pet by its key:
print(dictionary["cat"])
# you can edit the value:
dictionary["dog"] = "Taro"
print(dictionary)

# you can iterate a dictionary using a for loop (but you will not get it as ordered as it was defined)
for key in dictionary: # by default "key" will have the value of the key
    print("KEY=", key, "and its value=", dictionary[key])

print("\n---- using the keys method -----")
# the explicit default behavior, we can add the sorted function but is not required:
for key in sorted(dictionary.keys()): # basically is the same
    print("key:", key)

print("\n---- using the values method -----")
# or you can iterate over the values
for value in dictionary.values():
    print("value====", value)

print("\n---- using the items method -----")
# or get a tuple (key, value)
for key, val in dictionary.items():
    print(key, "--",  val)

print("\n---- adding elements -----")
# adding items. you just need to specify the new key and its value:
dictionary["my_new_key"] = ":D"
print(dictionary)

print("\n---- adding elements using the update method -----")
# adding items. you just need to specify the new key and its value:
dictionary.update({"helloooo":"my_value"})
print(dictionary)


print("\n---- delete elements -----")
# you can delete an item:
del dictionary["cat"]
print(dictionary)

print("\n---- delete the last item using the popitem method -----")
dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
dictionary.popitem()
print(dictionary)    # outputs: {'cat' : 'chat', 'dog' : 'chien'}

print("\n---- delete the whole dictionary and then try to access it -----")
# or delete the whole dictionary
print("ERROR OF COURSE:\n")
del dictionary
print(dictionary)
