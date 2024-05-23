produtos = ('Mouse', 640.49,
            'Teclado', 1000,
            'Monitor', 2100,
            'Mousepad', 150.75,
            'Computador', 7532)
print('='*50)
print(f'|{" LISTAGEM DE PREÇOS ":~^48}|')
print('='*50)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<40}', end='')
    else:
        print(f'R${produtos[pos]:>8.2f}')
print('='*50)