# main2.py

from sys import path

path.append('/home/noe/Documents/repos/learning_python/057_the__init.py__file/py/packages')

import extra.iota
from extra.good import alpha
print(extra.iota.FunI())
print(alpha.FunA())

from extra.iota import FunI


print(FunI())