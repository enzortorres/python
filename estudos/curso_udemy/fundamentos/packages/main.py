# from sys import path
# print(*path, sep='\n')

import main_package.module
print(main_package.module.soma_do_modulo(2,3)) 

from main_package import module
print(module.soma_do_modulo(2,3)) 

from main_package.module import soma_do_modulo
print(soma_do_modulo(2,3))

# ! MÁ PRÁTICA
from main_package.module import * 
print(soma_do_modulo(2,3))
