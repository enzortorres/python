from random import randint
from time import sleep

print('=' * 40)
print(f'{"JOGO NA MEGA SENA":^40}')
print('=' * 40)
lista = []
jogos = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1 
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(F'{" SORTEANDO {} JOGOS ".format(quant):=^40}')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1:^2}: {l}')
    sleep(0.8)
print(f'{" BOA SORTE ":=^40}')