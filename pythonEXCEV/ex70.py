total = mais = barato = cont = 0
itembarato = ' '
print('='*30)
print('{:^30}'.format('LOJA DO MUDINHO'))
print('='*30)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco >= 1000:
        mais += 1
    if cont == 1:
        barato = preco
    else:
        if preco < barato:
            barato = preco
            itembarato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'''O total da compra foi {total:.2f}
Temos {mais} produtos custando mais de R$1000.00
O produto mais barato foi {itembarato} que custa R${barato:.2f}''')
