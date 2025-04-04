lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

def somar_listas(lista_a, lista_b):
    return [
        x + y for x, y in zip(lista_a, lista_b)
    ]

print(somar_listas(lista_a,lista_b))


from itertools import zip_longest

print(
    [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)] # > Para pegar fazer a conta com a lista maior.
) # > "fillvalue=0" serve para preencher a lista menor com o valor 0 para nao ocorrer erros