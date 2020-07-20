"""
Python3 defines 63 built-in exceptions, and all of them form a
tree-shaped hierarchy, although the tree is a bit weird as its root is located on top.

BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
│   ├── ValueError
│   ├── AritmericError
│   │   └── ZeroDivisionError
│   └── LookupError
│       └── IndexError
│       └── KeyError
...

    ZeroDivisionError is a special case of more a general exception class named ArithmeticError;
    ArithmeticError is a special case of a more general exception class named just Exception;
    Exception is a special case of a more general class named BaseException;
"""
try:
    y = 1 / 0
except ArithmeticError: # Note that we have replaced ZeroDivisionError with ArithmeticError.
    print("Oooppsss...")
    #  ArithmeticError is a general class including (among others) the ZeroDivisionError exception

# You can branch a ZeroDivisionError but it will never be reached beacuse python takes the first match
# for that reason it is preferable to place specific exceptions at the begining
