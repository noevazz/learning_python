# Importing a module is done by an instruction named import.
import math # math is part of the Python standard library

# we can import multiple modules using multiple imports or using one:
import sys, random # these modules were imported juts to show you how to import do not pay much attention

# the other option is:
# import module1
# import module2
# import module3
# import moduleX

# now we can use the methods an variables of the math module:
print(math.pi)
# note that we need to use the name of the module + dot + the name of the function/method/variable/etc.

# btw if you want to know all the names provided through a particular module use the dir function:
print(dir(math)) # if the module's name has been aliased, you must use the alias, not the original name.

# if you want to use only a specific featur you can import only that feature:
from math import sin, radians
# with this kinf of import you are not required to use math.sin, just use sin()
print( sin( radians(90) ) ) 

# you can also use an alias:
from math import factorial as facto
print(facto(3))

# aliases are also for whole modules:
import random as ran
print(ran.randint(6, 10))

from math import sin as ss, radians as rr
print(rr(180))

# the most agresive import is when you import everything from a module:
from math import *
