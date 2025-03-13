# # ! EXERCÍCIO 1

tupla1 = (1, 2.5, 'Enzo', True)
print(tupla1[1], tupla1[3])

# tupla[2] = 10 # ? Não pode modificar, pois tupla é imutável

# ! EXERCÍCIO 2
tupla2 = (1,23,12,56,1)
print(f'O valor 1 foi encontrado {tupla2.count(1)} vezes na lista.')

# ! EXERCÍCIO 3
lista3 = [1,2,3,4,5]
lista3.append(100)
del(lista3[2])
lista3[0] = 500
print(lista3)

# ! EXERCÍCIO 4
notas = [10, 7, 5, 8, 3]
soma = sum(notas)
media = soma / len(notas)

print(f'Soma: {soma}\nMedia: {media}')

# ! EXERCÍCIO 5
lista5 = [300, 25, 15, 56, 74]
lista5.sort()
print(lista5)
lista5.sort(reverse=True)
print(lista5)
for i in range(len(lista5)):
    if lista5[i] > 10:
        print(lista5[i])

# ! EXERCÍCIO 6
lista6 = [[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]]
print(lista6[2][1])

somas = [0, 0, 0]
medias = []
for i in range(3):
    for j in range(4):
        somas[i] += lista6[i][j]
print(somas)

for i in range(3):
    medias.append(somas[i] / 4)
print(medias)
print(f'Maior media {max(medias)}')

# ! EXERCÍCIO 7
lista7 = []
for i in range(4):
    lista7.append(int(input("Digite um valor:")))

print(lista7.count(9))
print(lista7.index(3))
print('Valores pares: ', end='')

for i in range(len(lista7)):
    if lista7[i] % 2 == 0:
        print(lista7[i], end=' ')
print()

# ! EXERCÍCIO 8

import random

lista8 = [0] * 50
for i in range(50):
    lista8[i] = random.randint(1,6)

contagem_6 = lista8.count(6)
print(f'{contagem_6}/50')
porcentagem = (contagem_6 / 50) * 100
print(f'Com uma porcentagem de {porcentagem}%')
