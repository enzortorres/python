sal = float(input('Qual o seu salário? '))
if sal > 1250.00:
    aumento = sal + sal*0.10
    print('O seu salário recebeu um aumento de 10%, passou a ficar R${}'.format(aumento))
else:
    aumento = sal + sal*0.15
    print('O seu salário recebeu um aumento de 15%, passou a ficar R${}'.format(aumento))
