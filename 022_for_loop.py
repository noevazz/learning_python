# before jumping into the for loop:
# the range() function, it returns a sequence of numbers
# example: range(9) returns a sequence from 0 to 8
# example 2: range(1, 9) returns a sequence from 1 to 8

print(range(1,9))

# we can loop (iterate) the sequence using a for loop:
for my_item_in_range in range(1, 9): # any variable after the for keyword is the control variable 
    print(my_item_in_range) # code inside the foor will be executed each time for each item in the range
#                          each execution will update the control variable with the next item
#                          you don' neet to use the control variable if you don't want to, you may only want to execute a piece of code X times

# the range() function accepts anly integer values

# you can also iterate a string since:
for character in "hello world":
    if character == " ":
        continue
    print(character, ":D")
# you can also use break and continue and else (it works exactly the same as in a while loop)
