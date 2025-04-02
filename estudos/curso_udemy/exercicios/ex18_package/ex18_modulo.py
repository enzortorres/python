produtos = [
    {'nome': 'Produto 4', 'preco': 12.30,},
    {'nome': 'Produto 2', 'preco': 10.00,},
    {'nome': 'Produto 3', 'preco': 22.40,},
    {'nome': 'Produto 5', 'preco': 105.37,},
    {'nome': 'Produto 1', 'preco': 93.23,},
]

def exibir_lista(lista):
    for item in lista:
        nome = item['nome']
        preco_formatado = f'R${item['preco']:.2f}'.replace('.',',')
        print(f"Nome: {nome} | Preço: {preco_formatado}")
    print()