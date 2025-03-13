def linha(tam = 42):
    print('\n' + "=" * tam + '\n')

# # # ! tupla - um conjunto de dados imutáveis, é representado pelo () ou tuple()

# a = (1,2,3,4,'Marcelo', True)
# print(a)
# print(a[4])
# print(a[-3])
# print(a[1:5])
# print(a[3:])
# print(a[:4])

# # ? concatenar tuplas

# b = (1,2,3,4)
# c = (5,6,7)
# d = b + c

# print(f'A nova tupla: {d}')

# # ? len()
# aluno = ('Cora', 'Eliza', 'Olga', 'Marguerite', 'Cora')

# print(len(aluno))

# tamanho = len(aluno)

# for i in range(0, tamanho):
#     print(f'Oi, {aluno[i]}!')

# print(f'O nome Cora foi localizado {aluno.count('Cora')} vezes')

# # ! lista - um conjunto de dados mutáveis, é presentado pelo [] ou list()

# nomes = ['Cora', 'Eliza', 'Olga', 'Marguerite', 'Cora']

# nomes[4] = 'Enzo'

# print(nomes[4])

# # ? append() - adiciona novos valores no final da lista

# nomes.append('Natan')

# print(nomes)

# estados = []
# estados.append(input("Digite o seu estado: "))

# estados.insert(1, 'Enzo')

# numeros = [61,78,95,54,82,11]

# notas = []
# for i in range(0, 3):
#     notas.append(float(input(f"Digite a {i+1} nota:")))
# media = sum(notas) / len(notas)
# print(f"Media: {media:.1f}")

# var = notas.pop()
# print(var)

# ? dicionários ----------------------------------------------------------------

filme = {
    'titulo': 'Moana',
    'ano': 2016,
    'autor': 'John Musker'
}

print(filme.keys())
print(filme.values())
print(filme.items())

for chave in filme.keys():
    print(f'Chave: {chave}')
    
for valor in filme.values():
    print(f'Valor: {valor}')
    
for item in filme.items():
    print(f'Item: {item}')
    
for chave, valor in filme.items():
    print(f'Chave: {chave}\nValor: {valor}\n')

# ? update() -----------------------------------------------------------

dict2 = {'nome' : 'Enzo'}
print(dict2)

dict2.update({'nome': 'Enzo Ribas'}) # ? Para atualizar o nome
print(dict2)

dict2.update({'idade': 20}) # ? Para atualizar inserindo nova chave e valor
print(dict2)

a = {'a': 1, 'b': 2, 'c': 3}
b = {'d': 4}
print(a)

a.update(b) # ? Para concatenar dicionários
print(a)

# ? copy() ------------------------------------------------------

original = {'a': 1, 'b': 2, 'c': 3}
copia = original.copy()

linha()
print(original)
print(copia)

linha()
copia['e'] = 8
print(original)
print(copia)

lista_pessoa = []

for i in range(2):
    pessoa = {
        'nome': str(input("Digite o nome: ")),
        'idade': int(input("Digite a idade: ")),
        'email': str(input("Digite o email: ")),
    }
    lista_pessoa.append(pessoa.copy())

for item in lista_pessoa:
    for chave, valor in item.items():
        print(f"{chave}: {valor}")
    print()