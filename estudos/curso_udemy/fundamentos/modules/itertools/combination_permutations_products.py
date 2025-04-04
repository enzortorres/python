from itertools import combinations, permutations, product

"""
    | Combinations. Permutations e Product - Itertools
    ? Combinação - Ordem não importa - iterável + tamanho do grupo
    ? Permutação - Ordem importa
    ? Produto - Ordem importa e repete valores únicos
"""

def print_iter(iterator): 
    print(*list(iterator), sep="\n")
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unissex'],
    ['algodão', 'poliéster'],
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))