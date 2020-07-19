def wrapper_1(fun):
    def before():
        print("Before")

    def after():
        print("After")

    def new_functionality():
        before()
        fun()
        after()
    
    return new_functionality

@wrapper_1
def simple_fun():
    print("Hi I'm being decorated")

simple_fun()
print("----")

# This wrapper is so simple that I can even use it in other functions:

@wrapper_1
def other():
    print("wadup bro")

other()
print("----")

# complex wrappers 2

def wrapper_2(fun):
    def more_things():
        return  fun()
        # we could do result=fun and then return result, but it's the same 
    return more_things

@wrapper_2
def function_that_returns_something():
    print("hello")
    return ":D"

print(function_that_returns_something())

# complex wrapper 3
def wrapper_3(f):
    def more(*args, **kwargs):
        print("before")
        f(*args, **kwargs)
        print("after")
    return more

@wrapper_3
def operation(a,b,c):
    print(a*b*c)

operation(1,2,2)
print("----")

# complex wrappers 4
def wrapper_4(argument1):
    def _wrapper_4(fun):
        def more_and_more(*args, **kwargs):
            print("before", argument1)
            fun(*args, **kwargs)
            print("after")
        return more_and_more
    return _wrapper_4

@wrapper_4(argument1= 12345)
def hi(a,b,c):
    print(a+b+c)

hi(1,2,2)
print("----")