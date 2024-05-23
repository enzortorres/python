# Utilizando o while
from math import factorial
num = int(input('\033[33mDigite um valor para descobrir seu fatorial:\033[30m '))
fatorial = factorial(num)
c = num
print('\033[34mCalculando:\033[32m {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1 
print('{}'.format(fatorial),end='')

# Utilizando o for
#from math import factorial
#num = int(input('Digite um valor para descobrir seu fatorial: '))
#fatorial = factorial(num)
#print('Calculando: {}! = '.format(num), end='')
#for c in range(1, num+1):
#    print('{}'.format(num), end='')
#    print(' x ' if num >
#           1 else ' = ', end='')
#   num -= 1
#print('{}'.format(fatorial))