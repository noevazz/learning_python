print("-------------------- and ---------------------")
print("""and is a logical conjunction operator
It's a binary operator with a priority that is lower than the one expressed by the comparison operators.
It allows us to code complex conditions without the use of parentheses like this one:""")
print("""
    Sample code:
        if 10>3 and 3 in range(20):
            print("Both are True")
    Execution:""")
if 10<3 and 3 in range(20):
    print("Both are True")
print('Truth table of "and":')
print("True and True = False")
print("any other conbination is False")

print("\n--------------------- or -------------------")
print("is a disjunction operator. It's a binary operator with a lower priority than and (just like + compared to *)")
print("Truth table:")
print(
"""True  or True = True
True  or False = True
False or True = True
False or False = False""")

print("\n------------------- not --------------------")
print("It's a unary operator performing a logical negation.")
print("Truth table:")
print("""\
not True  = False
not False = True""")

print("\n----------- Bitwise operations --------------")
print('& bitwise conjuntion (BIT A BIT "and")')
print("| bitwise disjunction")
print("^ bitwise exclusive or (xor)")
print(
"""\
  ArgA	ArgB	ArgB&ArgB	ArgA|ArgB	ArgA^ArgB
    0     0         0               0               0
    0     1         0               1               1
    1     0         0               1               1
    1     1         1               1               0""")

print("\n---------bitwise negation(complement) ~ ------------")
print("basically: ~x = -x-1")
print("~0=", ~0)
print("~1=", ~1)
print("~128=", ~128)

print("\n--------------bitwise left-shit << ------------------")
print("2<<3=", 2<<3)
print("in other words 10(2 in binary) moved 3 spaces to the left: 10000")

print("\n-------------bitwise right-shift >> -----------------")
print("16>>2=", 16>>2)
print("in other words: 10000 (16 in binary) moved 2 spaces to the right 100")

