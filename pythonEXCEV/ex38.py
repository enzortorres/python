n1 = int(input('\033[0;33mDigite um valor: \033[m'))
n2 = int(input('\033[0;33mDigite outro valor: \033[m'))

if n1 == n2:
    print('\033[0;31mNão \033[0;33mexiste valor maior, os dois são iguais.\033[m')
elif n1 > n2:
    print('\033[0;33mO primeiro valor é maior.\033[m')
else:
    print('\033[0;33mO segundo valor é maior.\033[m')