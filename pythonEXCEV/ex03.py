n1 = int(input('\033[33mDigite um valor:\033[30m '))
n2 = int(input('\033[33mDigite outro valor:\033[30m '))
soma = n1 + n2
print('\033[34mA soma de \033[31m{}\033[34m e \033[31m{}\033[34m é \033[31m{}\033[34m!\033[m'.format(n1, n2, soma))