lista = ['Noah', 'Lawrence', 'Lois']
lista.append('Lulu')

print('\n' + '=' * 50 + '\n')

for item in enumerate(lista):
    index, nome = item
    print(index, nome)

print('\n' + '=' * 50 + '\n')

lista_enumerada = list(enumerate(lista, start=1))
print(lista_enumerada)

print('\n' + '=' * 50 + '\n')
