```
---------- Understanding Exceptions ----------
Each time your code tries to do something
wrong/foolish/irresponsible/crazy/unenforceable,
Python does two things:
       - it stops your program;
       - it creates a special kind of data, called an exception.

---------- DEFINITION ----------
Both of these activities are called raising an exception.
We can say that Python always raises an exception (or that an exception has been raised)
when it has no idea what do to with your code.

---------- What happens netx? ----------
       - The raised exception expects somebody or something to notice it and take care of it;
       - If nothing happens to take care of the raised exception, the program will be forcibly
         terminated, and you will see an error message
       - Otherwise, if the exception is taken care of and handled properly,
        the suspended program can be resumed and its execution can continue.

You know some exception names already:
       ValueError: math domain error 
ValueError is the exxception name
```