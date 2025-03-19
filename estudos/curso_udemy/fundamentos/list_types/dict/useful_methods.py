"""
    | Métodos úteis dos dicionários em python
    ? len - retorna quantas chaves tem no dicionário
    ? keys - iterável com as chaves
    ? values - iterável com os valores
    ? items - iterável com as chaves e valores
    ? setdefault - adicionar valor se a chave não existe
    ? copy - retorna uma cópia rasa (shallow copy)
    ? get - obtém uma chave
    ? pop - apaga um item com a chave específicada (del)
    ? popitem - apaga o último item adicionado
    ? update - atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Enzo',
    'sobrenome': 'Ribas',
}

pessoa.setdefault('idade', 0)

print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))

nome = pessoa.pop('nome')
print(nome)
print(pessoa)

pessoa.update({
    'nome': 'Enzo',
    'sobrenome': 'Torres',
    'altura': 1.8,
})

print(pessoa)

