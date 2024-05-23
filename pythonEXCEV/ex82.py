list = []
pares = []
ímpares = []
while True:
    num = (int(input('Digite um valor: ')))
    list.append(num)
    resp = ' '
    while not resp in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
for  i, v in enumerate(list):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'''A lista completa é {list}
A lista de pares é {pares}
A lista de ímpares é {ímpares}''')
