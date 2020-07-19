# if you want to use a global variable inside a function you can use the global keyword:
def myFunction():
    global var
    var = "new value"

var = "old value"
myFunction()
print(var)

# But remember that if you are passing a reference (list) you can edit it, but this is only a special case