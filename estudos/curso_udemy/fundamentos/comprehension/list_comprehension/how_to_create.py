lista = []
for numero in range(10):
    lista.append(numero)
    
lista_2 = list(range(1, 11))
print(lista, lista_2)

lista = [numero if numero % 2 == 0 else '' 
        for numero in range(10)]
print(lista)

# ? Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.10 # > Para aumentar o preço de cada produto em 10%
    if produto['preco'] > 20 else {**produto}} # > Para aumentar somente o preço para os produtos com preço maior do que 20
    for produto in produtos
]

print(*novos_produtos, sep='\n')