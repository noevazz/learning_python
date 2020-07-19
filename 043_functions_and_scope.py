# if you call a variable that is defined inside a function in othe place it will raise and error since it does NOT exist,
# it only existe inside the function
def scopeTest():
    x = 123

scopeTest()
print(x) # ERROR: NameError: name 'x' is not defined