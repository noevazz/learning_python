"""
An additional, possible branch can be placed inside (or rather, directly behind) the try-except block
A code labelled in this way is executed when (and only when) no exception has been raised inside the try:
"""
try:
    n = 1 / 2
except ZeroDivisionError:
    print("Division failed")
else:
    print("Everything went fine")


"""
The finally block is always executed (it finalizes the try-except block execution, hence its name),
no matter what happened earlier, even when raising an exception, no matter whether this has been handled or not.
"""
try:
    n = 1 / 0
except ZeroDivisionError:
    print("Division failed")
#else:   #else and finally can coexist, uncomment these lines and check ;)
#    print("Everything went fine")
finally:
    print("I don't care what happeded, I will say HI!")
