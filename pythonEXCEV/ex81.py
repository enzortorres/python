list = []
while True:
    list.append(int(input('Digite um valor: ')))
    resp = ' '
    while not resp in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Ao total você digitou {len(list)} números.')
list.sort(reverse=True)
print(f'A lista de valores ordenada de forma decrescente é {list}.')
list.sort()
if 5 in list:
    print(f'O valor 5 foi encontrado na lista e está na {list.index(5)} posição.')
else:print('O valor 5 não foi encontrado na lista.')
