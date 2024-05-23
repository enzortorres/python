preco = float(input('Qual o preço do produto? '))
porcentagem = preco/1/20
desconto = preco - porcentagem
print('O valor do produto com o desconto fica: {}'.format(desconto))
print('-'*50)
salario = float(input('Qual o salário do funcionário? '))
print('-'*50)
porcentagem = salario*3/20
aumento = salario + porcentagem
print('O salário do funcionário x, passou a ser {} com o aumento.'.format(aumento))
print('-'*50)


