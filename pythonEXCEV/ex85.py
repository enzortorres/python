num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=' * 30)
num[0].sort()
num[1].sort()
print(f'''Os valores pare digitados foram: {num[0]}
Os valores ímpares digitados forma: {num[1]}''')

