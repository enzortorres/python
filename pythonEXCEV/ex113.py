from ex113function import *
n1 = n2 = 0
try:
    n1 = leiaInt('Digite um Inteiro: ')
    n2 = leiaFloat('Digite um Real:')
except (KeyboardInterrupt, TypeError):
    print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
finally:
    print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')