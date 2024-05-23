dias = int(input('Quantos dias alugados? '))
km = float(input('Quando Km rodados? '))
precodia = dias * 60
precokm = 0.15 * km
precototal = precodia + precokm
print(f'O total a pagar é de R${precototal:.2f}')