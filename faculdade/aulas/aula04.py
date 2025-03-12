# # ! tupla - um conjunto de dados imutáveis, é representado pelo () ou tuple()

a = (1,2,3,4,'Marcelo', True)
print(a)
print(a[4])
print(a[-3])
print(a[1:5])
print(a[3:])
print(a[:4])

# ? concatenar tuplas

b = (1,2,3,4)
c = (5,6,7)
d = b + c

print(f'A nova tupla: {d}')

# ? len()
aluno = ('Cora', 'Eliza', 'Olga', 'Marguerite', 'Cora')

print(len(aluno))

tamanho = len(aluno)

for i in range(0, tamanho):
    print(f'Oi, {aluno[i]}!')

print(f'O nome Cora foi localizado {aluno.count('Cora')} vezes')

# ! lista - um conjunto de dados mutáveis, é presentado pelo [] ou list()

nomes = ['Cora', 'Eliza', 'Olga', 'Marguerite', 'Cora']

nomes[4] = 'Enzo'

print(nomes[4])

# ? append() - adiciona novos valores no final da lista

nomes.append('Natan')

print(nomes)

estados = []
estados.append(input("Digite o seu estado: "))

estados.insert(1, 'Enzo')

numeros = [61,78,95,54,82,11]

notas = []
for i in range(0, 3):
    notas.append(float(input(f"Digite a {i+1} nota:")))
media = sum(notas) / len(notas)
print(f"Media: {media:.1f}")

notas.pop()

