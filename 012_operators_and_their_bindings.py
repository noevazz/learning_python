# The binding of the operator determines the order of computations performed by some operators with equal priority, put side by side in one expression.
print(9 % 6 % 2)
# This operator has left-sided binding
# 9%6=3, then 3%2=1, result=1

print("example with right-sided binding:")
print(2 ** 2 ** 3)
# first 2**3=8, then 2**8=256, result=256
