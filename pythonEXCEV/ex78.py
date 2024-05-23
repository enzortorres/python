maior = menor = 0
list = []
for c in range(0, 5):
    list.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = list[c]
    else:
        if list[c] > maior:
            maior = list[c]
        if list[c] < menor:
            menor = list[c]
print('=-'*30)
print(f'Você digitou os valores {list}')
print(f'O maior número digitado foi {maior} nas posições ', end='')
for i, v in enumerate(list):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(list):
    if v == menor:
        print(f'{i}... ', end='')
print()