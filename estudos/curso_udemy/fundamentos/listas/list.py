"""
    | Listas em Python
    * Tipo list - Mutável
    * Suporta vários valores de qualquer tipo
    * Métodos úteis: 
    * append - Adiciona um valor ao final da lista
    * insert - Adiciona um valor em um lugar específico da lista
    * pop    - Remove o último valor da lista
    * del    - Apaga um valor da lista
    * clear  - Limpa a lista por completo 
    * extend - Estende a lista
    * Create Read Update Delete (CRUD)
"""

def linha(tam = 42):
    print("-" * tam)

lista   = [123, True, 123.3, 'Enzo', [12345, False, 321.1, 'Ribas']]

print(lista)
linha()

del lista[2]
lista.remove(123) # ? Remove um valor específico da lista
print(lista)
linha()

print(lista[2])
print(lista[2][0])
linha()

lista.append(3) # ? Adiciona ao final da lista
print(lista)
linha()

lista.insert(3, 56) # ? Insere um valor num lugar específico da lista
print(lista)
linha()

valor_removido = lista.pop() # ? Remove o último valor da lista e retorna para uma variavél (opcional)
print(f"Valor removido: {valor_removido}")
print(lista)
linha()

lista.clear() # ? Limpa a lista por completo
print(lista)
linha()
