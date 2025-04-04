def zipper(estados, uf):
    lista = [
        (estados[i], uf[i]) for i in range(min(len(estados), len(uf)))
    ]
    return lista

estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
uf = ['BA', 'SP', 'MG', 'RJ']

from itertools import zip_longest

print(zipper(estados, uf)) 
print(list(zip(estados, uf))) # > Utiliza a lista menor como referência
print(list(zip_longest(estados, uf))) # > Utiliza a lista maior como referência
