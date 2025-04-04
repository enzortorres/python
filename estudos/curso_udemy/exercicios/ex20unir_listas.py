def zipper(estados, uf):
    lista = [
        (estados[i], uf[i]) for i in range(min(len(estados), len(uf)))
    ]
    return lista

estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
uf = ['BA', 'SP', 'MG', 'RJ']

print(zipper(estados, uf))