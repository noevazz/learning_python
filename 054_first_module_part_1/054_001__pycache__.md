```
when you execute main.py you should see a directory that was created after this: __pycache__
inside this directory there should be a file called module.cpython-xy.pyc
    module is the name of the module "module"
    where x and y are digits derived from your version of Python
    cpython is the Python implementation
    The last part (pyc) comes from the words Python and compiled.

You can look inside the file - the content is completely unreadable to humans.
It has to be like that, as the file is intended for Python's use only.

When Python imports a module for the first time, it translates its contents into a somewhat compiled shape.
The file doesn't contain machine code - it's internal Python semi-compiled code, ready to be executed by
Python's interpreter. As such a file doesn't require lots of the checks needed for a pure source file,
the execution starts faster, and runs faster, too.

Thanks to that, every subsequent import will go quicker than interpreting the source text from scratch.

Python is able to check if the module's source file has been modified (in this case, the pyc file will be rebuilt)
or not (when the pyc file may be run at once). As this process is fully automatic and transparent, you don't have to keep it in mind.
```