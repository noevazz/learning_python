class Level1:
    var = 100
    def fun(self):
        return 101

class Level2(Level1):
    var = 200 # it overwrites the father's
    def fun(self): # it overwrites the father's
        return 201

class Level3(Level2):
    pass

obj = Level3()

print(obj.var, obj.fun())
