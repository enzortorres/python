from datetime import date
atual = date.today().year
ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['idade'] = atual - int(input('Ano de nascimento: '))
ficha['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if ficha['ctps'] != 0:
    ficha['ano'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Salário: '))
    ficha['aposentadoria'] = ficha['idade'] + 35
print('-=' * 20)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}.')
