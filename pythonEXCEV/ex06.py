n = int(input('\033[33mDigite um número:\033[30m] '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print(f'''\033[34mO dobro de \033[31m{n}\033[34m vale \033[31m{dobro}
\033[34mO triplo de \033[31m{n}\033[34m vale \033[31m{triplo}
\033[34mA raiz quadrada de \033[31m{n}\033[34m é igual a \033[31m{raiz}\033[m''')