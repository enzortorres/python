lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
lanche.append('Cookie')
print(lanche)
lanche.insert(0,'Cachorro quente')
print(lanche)
lanche.remove('Pizza')
print(lanche)
lanche.pop()
print(lanche)
if 'Pizza' in lanche:
    lanche.remove('Pizza')
valores = list(range(4, 11))
valores.sort()

print(valores)
print(len(valores))