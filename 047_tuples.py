# tuples are sequence that are immutables
my_first_tuple = (10, 11, 12, 13)
# tuples are defined with parenthesis
empty_tuple = ()
# buuuut, you can create a tuple with only commas:
other_tuple = 1,2,3,4,5,6
print("other_tuple=", other_tuple)

# tuples with one element are defined with a comma at the end of the unique value:
small_tuple = (10,)
another_valid_way = 90,
print("another_valid_way=", another_valid_way)
# because if you do NOT use that comma it will be treated as a scalar:
print( type( (23,) ) )
print( type( (23) ) )

# since tuples are immutable you can not edit (update, delete) an item
#    the len() function accepts tuples, and returns the number of elements contained inside;
#    the + operator can join tuples together (we've shown you this already)
#    the * operator can multiply tuples, just like lists;
#    the in and not in operators work in the same way as in lists.

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

nice_tuple = (2,5,6) * 3 # this will create ONE (not three) big tuple:
print(nice_tuple)
# slicing techniques are preserved