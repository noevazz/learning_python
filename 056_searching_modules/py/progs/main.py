from sys import path

path.append('/home/noe/Documents/repos/learning_python/056_searching_modules/py/modules')
# with windows system you need to use \\
import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
