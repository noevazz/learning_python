# The random module delivers some mechanisms allowing you to operate with pseudorandom numbers.

# The algorithms aren't random - they are deterministic and predictable.
# Only those physical processes which run completely out of our control (like the intensity of cosmic radiation)
# may be used as a source of actual random data.
# Data produced by deterministic computers cannot be random in any way.

# A random number generator takes a value called a seed, treats it as an input value, calculates a "random" number
# based on it (the method depends on a chosen algorithm) and produces a new seed value.

from random import random, seed, randrange, randint, choice, sample

print("\n----- the random method -----")
# random() (not to be confused with the module's name) produces a float number x coming from the range (0.0, 1.0)
# in other words: (0.0 <= x < 1.0)
print(random())

print("\n----- the randint function -----")
# returns a number between x and y (both included):
print(randint(9, 20))

print("\n----- the randrange function -----")
# returns a number between x and y (y is not included):
print(randrange(9, 20))

print("\n----- the choice function -----")
# chooses a "random" element from the input sequence and returns it
print( choice( [2,5,12,6,929,0,5] ) )

print("\n----- the sample function -----")
# sample(sequence, elements_to_choose=1)
#  builds a list (a sample) consisting of the elements_to_choose element (which defaults to 1) "drawn" from the input sequence.
print( sample( [2,5,12,6,929,0,5], 4 ) )


print("\n----- the seed function -----")
# The seed(int_value) function is able to directly set the generator's seed. We'll show you two of its variants:
seed(2)
for i in range(5):
    print(random())
# Due to the fact that the seed is always set with the same value, the sequence of generated values always looks the same.
#     Execute the program again and you will have the same "random" numbers