salario = float(input('\033[33mQual o salário do funcionário? \033[4;32mR$'))
taxa = salario * 0.15
aumento = salario + taxa
print(f'\033[0;34mUm funcionário que recebia \033[4;32mR${salario:.2f}\033[0;34m, com \033[31m15%\033[34m de aumento, passa a receber \033[4;32mR${aumento:.2f}\033[34m!\033[m')