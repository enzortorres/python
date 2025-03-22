produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

for chave, valor in produto.items():
    print(chave, valor)

dc = {
    chave: valor
    for chave, valor
    in produto.items()
}

print(dc)