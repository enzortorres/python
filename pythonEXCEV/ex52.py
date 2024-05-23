valor = int(input('\033[4;30mDigite um valor:\033[m '))
total = 0
for c in range(1 , valor + 1):
    if valor % c == 0:
        print('\033[36m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\033[33mO número {} foi divisível {} vezes\033[m'.format(valor, total))
if total == 2:
    print('\033[4;32mE por isso ele é primo!\033[m')
else:
    print('\033[4;31mE por isso ele não é primo!\033[m')