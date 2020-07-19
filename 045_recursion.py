# recursion is when you invoke a function inside the same function:
def factorialFun(n): # Factorial of N number is equal to N*(N-1)*(N-2) ... *(1)
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)

print(factorialFun(3))

# Yes, there is a little risk indeed. If you forget to consider the conditions which
# can stop the chain of recursive invocations, the program may enter an infinite loop. You have to be careful.