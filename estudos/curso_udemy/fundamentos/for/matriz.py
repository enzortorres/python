tamanho = 5

for i in range(tamanho):
    for j in range(tamanho):
        if i + j == tamanho - 1:
            print('[ * ]', end='')
        else:
            print('[   ]', end='')
    print()