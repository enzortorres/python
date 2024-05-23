list = []
while True:
    number = int(input('Digite um valor: '))
    if number not in list:
        list.append(number)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Tente novamente!')
    resp = ' '
    while not resp in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('=-'*20)
list.sort()
print(f'Você digitou os valores {list}')