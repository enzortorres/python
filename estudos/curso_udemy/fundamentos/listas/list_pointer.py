lista_a = ['Enzo', 'Ribas']
lista_b = lista_a # ? Aponta para o mesmo endereço de memória da variável

lista_a.append("Torres")

print(lista_a)
print(lista_b)

print('-' * 50)

lista_a = ['Enzo', 'Ribas']
lista_b = lista_a.copy() # ? Copia a lista para a variável

lista_a.append("Torres")

print(lista_a)
print(lista_b)

