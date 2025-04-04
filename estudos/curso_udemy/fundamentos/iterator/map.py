from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
    }

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# > Caso queira de reutilizar o iterator, precisa transformar em lista
novos_produtos = list(map( # > List para transformar o iterator em lista, pois o iterator esgota
    muda_preco_de_produtos,
    produtos
))

# novos_produtos = (x for x in produtos) # > Generator

# novos_produtos = [
#     {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
# ]

print_iter(produtos)
print_iter(novos_produtos)

print(novos_produtos)
print(hasattr(novos_produtos, "__iter__"))
print(hasattr(novos_produtos, "__next__"))
print(isinstance(novos_produtos, GeneratorType))

print(
    list(map(
    lambda x: x * 3,
    [1,2,3,4]
)))