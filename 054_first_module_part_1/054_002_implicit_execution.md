```
When a module is imported, its content is implicitly executed by Python.
It gives the module the chance to initialize some of its internal aspects
(e.g., it may assign some variables with useful values). Note: the initialization
takes place only once, when the first import occurs, so the assignments done by the module aren't repeated unnecessarily.

That's why the execution of the main.py file outputs "I like to be a module"

You can note this code in module.py:
if __name__ == "__main__":
    print("hello from inside the module")

Python creates a variable called __main__ for each file, when you execute a file its value will be the same as "__main__"
that's why when you execute the main.py file you do NOT see "hello from inside the module".
if you get __name__ from outside a module, the value of that variable will be the name of the file containing that module (wuthout the .py extension)
```
