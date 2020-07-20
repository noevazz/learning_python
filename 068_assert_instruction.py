"""
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
│   ├── AssertionError
│   ├── ...
...
"""

import math

x = float(input("Enter a number: "))
assert x >= 0.0 # negative values will raise an AssertionError
"""
assert evaluates the expression,
assert won't do anything if the expression evaluates to
    True
    a non-zero numerical value
    a non-empty string
    any other value different than None
Otherwise, it automatically and immediately raises an exception named AssertionError
(in this case, we say that the assertion has failed)
"""

# you may want to put it into your code where you want to be
# absolutely safe from evidently wrong data:
x = math.sqrt(x)

print(x)