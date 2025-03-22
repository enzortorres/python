from pprint import pprint

def p(v):
    pprint(v, sort_dicts=False, width=40)

# ? Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.10} # > Para aumentar o preço de cada produto em 10%
    if produto['preco'] > 20 else {**produto} # > Para aumentar somente o preço para os produtos com preço maior do que 20
    for produto in produtos
]

# print(*novos_produtos)
lista = [n for n in range(10)
        if n < 5 # > Só atribuir numeros que forem menor do que 5
        ]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.10} # > Para aumentar o preço de cada produto em 10%
    if produto['preco'] > 20 else {**produto} # > Para aumentar somente o preço para os produtos com preço maior do que 20
    for produto in produtos
    if produto['preco'] >= 20 and produto['preco'] > 10 # > Para atribuir somente valores maiores do que 10
]
p(novos_produtos)


lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
        
lista = [
    (x,y) # > Oque vai atribuir na lista
    for x in range(3) 
    for y in range(3)
]

lista = [
    [(x,y) for y in range(3)]
    for x in range(3) 
]

print(lista)

for item in lista:
    print(item)