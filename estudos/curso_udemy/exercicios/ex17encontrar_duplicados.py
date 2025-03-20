"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

# ! Primeira tentativa - ERRO
# def primeiro_duplicado(lista): 
#     index = 0
#     menor_distancia = 0
#     index_menor_distancia = 0
#     tem_duplicado = False

#     for i in range(len(lista)):
#         distancia = 0
#         for j in range(index + 1, len(lista)):
#             if lista[index] != lista[j]:
#                 distancia += 1
#             else:
#                 tem_duplicado = True
#                 if distancia < menor_distancia or menor_distancia == 0:
#                     menor_distancia = distancia
#                     index_menor_distancia = index
#                 break
#         index += 1
#     if tem_duplicado:
#         return lista[index_menor_distancia]
#     return -1

# ! Segunda tentativa - ACERTO
def primeiro_duplicado(lista):
    numeros_vistos = set()
    
    for num in lista:
        if num in numeros_vistos:
            return num
        numeros_vistos.add(num)
    return -1
    
for lista in lista_de_listas_de_inteiros:
    print(lista, primeiro_duplicado(lista))