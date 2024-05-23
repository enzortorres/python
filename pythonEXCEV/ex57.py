sexo = str(input('\033[33mInforme seu sexo: [M/F]\033[30m ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('\033[31mDados inválidos!\033[33m Informe o seu sexo: [M/F]\033[30m ')).strip().upper()[0]
print('\033[32mSexo {} anotado com sucesso! :)\033[m'.format(sexo))
