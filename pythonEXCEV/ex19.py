from time import sleep
from random import choice
a1 = str(input('\033[33mPrimeiro aluno:\033[30m '))
a2 = str(input('\033[33mSegundo aluno:\033[30m '))
a3 = str(input('\033[33mTerceiro aluno:\033[30m '))
a4 = str(input('\033[33mQuarto aluno:\033[30m '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('\033[34mSorteando em \033[31m3... ', end='')
sleep(1)
print('\033[33m2... ', end='')
sleep(1)
print('\033[32m1...')
sleep(1)
print(f'\033[34mO aluno escolhido foi: \033[4;35m{escolhido}\033[m')