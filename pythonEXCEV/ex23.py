n = int(input('Informe um número: '))
print(f'Analisando o número {n}')
uni = n // 1 % 10
dez = n // 10 % 10
cent = n // 100 % 10
milhar = n // 1000 % 10
print(f'''Unidade: {uni}
Dezena: {dez}
Centena: {cent}
Milhar: {milhar}''')