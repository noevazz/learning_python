```
There's a special variable (actually a list) storing all locations (folders/directories)
that are searched in order to find a module which has been requested by the import instruction.

The variable is named path, and it's accessible through the module named sys

we've used the append() method - in effect, the new path will occupy the last element in the path list; if you don't like the idea, you can use insert() instead.

from the main.py file:
    from sys import path
    path.append('/home/noe/Documents/repos/learning_python/056_searching_modules/py/modules') # confirm the module path was added with print(path)

    import module # now we can import the module

```