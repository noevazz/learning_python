# The number-string conversion is simple, as it is always possible. It's done by a function named str()
int_num = 13
float_num = 1.3
sint = str(int_num)
sfloat = str(float_num)

print(sint + ' ' + sfloat)

# string-number is possible when and only when the string represents a valid number.
# If the condition is not met, expect a ValueError exception.
string_int = '13'
string_float = '1.3'
istring = int(string_int)
fstring = float(string_float)

print(istring + fstring)
