from sys import path 

import import_package.modulo
from import_package import modulo
from import_package.modulo import *

print(soma(1,2))
print(import_package.modulo.soma(1,2))
print(modulo.soma(1,2))