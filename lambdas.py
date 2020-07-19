# lambdas are anonymous functions

# Sintax
#     lambda arguments : expression
#     the result of the expression is what we will have if we execute the lambda
# Example
#     lambda x, y : x*3 + y

# A lambda returns a <lambda> function, we can assing this to a variable:

my_first_lambda = lambda number : number * 100

# Now we can use the varibale my_fir_lambda:

print(my_first_lambda(3))
print(my_first_lambda(55))

# we can pass more arguments to a lambda:
greeting = lambda your_name, my_name : f"hi {your_name}, I am {my_name}"

print(greeting("andy", "noe"))
print(greeting("lalisa", "andru"))

# we can also use a lambda as a return value in a function:

def operation(number):
    return lambda a, b, c : number * (a+b+c)

op1 = operation(5)
# Line above is the same as op1 = lambda a, b, c : 5 * (a+b+c)
#     This means that we can use op1(a,b,c):
print(op1(1,2,3))

# this allows us to use "lambda a,b,c:number*(a+b+c)"
#     with different values for a,b,c and number:

op2 = operation(0.5)
# Remember, line above is the same as op2 = lambda a,b,c: 0.5*(a+b+c)
print(op2(3, 2, 5))

# This can be a way to reuse one lambda and then
# set different values for the arguments and expression
