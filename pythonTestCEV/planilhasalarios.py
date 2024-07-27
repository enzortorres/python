print("-"*50)
print('Planilha salário funcionários Tutti Amici')
print("-"*50)
adriane = 10000.00
guilherme = 10000.00
vitor = 1000.00
bruno = 2000.00
enzo = 1000.00
funcionario = str(input('Deseja checar o salário de qual funcionário? '))
if funcionario == 'adriane':
    print("-"*50)
    print('O(a) funcionário(a) {} tem um salário de '.format(funcionario), adriane,)
    print("-"*50)
    funcionario = adriane
if funcionario == 'guilherme':
    print("-"*50)
    print('O(a) funcionário(a) {} tem um salário de '.format(funcionario), guilherme,)
    print("-"*50)
    funcionario = guilherme
if funcionario == 'vitor':
    print("-"*50)
    print('O(a) funcionário(a) {} tem um salário de '.format(funcionario), vitor,)
    print("-"*50)
    funcionario = vitor
if funcionario == 'bruno':
    print("-"*50)
    print('O(a) funcionário(a) {} tem um salário de '.format(funcionario), bruno,)
    print("-"*50)
    funcionario = bruno
if funcionario == 'enzo':
    print("-"*50)
    print('O(a) funcionário(a) {} tem um salário de '.format(funcionario), enzo,)
    print("-"*50)
    funcionario = enzo

change = input('Deseja fazer alguma mudança? ')
print("-"*50)
if change == 'sim':
    changea = input('Deseja fazer que tipo de mudança? ')
    print("-"*50)
    if changea == 'aumento':
        aumento = int(input('Quanto deseja aumentar? '))
        print("-"*50)
        porcentagem = funcionario * aumento/100
        novosalarioa = funcionario + porcentagem
        print('O salário de {} passou a ser: {}'.format(funcionario, novosalarioa))
        print("-"*50)
if changea == 'corte':
    corte =float(input('Quanto deseja cortar? '))
    print(' '*50)
    porcentagem = funcionario * corte/100
    novosalarioc = funcionario - porcentagem
    print('O salário de {} passou a ser: {}'.format(funcionario, novosalarioc))
    print("-"*50)