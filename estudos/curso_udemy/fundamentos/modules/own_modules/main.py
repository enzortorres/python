import sys
import importlib

import module

print('Este módulo se chama', __name__)
print('Importei o módulo:', module.__name__)

from module import soma, variavel_modulo

print(soma(2,3))
print(variavel_modulo)

# if __name__ == '__main__':
#     print('main')
# else:
#     print('erro')