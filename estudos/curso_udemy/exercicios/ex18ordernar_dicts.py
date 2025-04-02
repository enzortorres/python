from ex18_package import produtos, exibir_lista
from copy import deepcopy

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.10, 2)} # > retorna o produto com aumento de 10% e formatado em 2 casas decimais
    for produto in deepcopy(produtos)
]

produtos_ordenados_por_nome = sorted(
    deepcopy(novos_produtos),
    key=lambda item: item['nome'], reverse=True
)
produtos_ordenados_por_preco = sorted(
    deepcopy(novos_produtos),
    key=lambda item: item['preco']
)

print('Produtos originais')
exibir_lista(produtos)

print('Produtos ordenado por nome decrescente')
exibir_lista(produtos_ordenados_por_nome)

print('Produtos ordenado pelo preco crescente')
exibir_lista(produtos_ordenados_por_preco)
