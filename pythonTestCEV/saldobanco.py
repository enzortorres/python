total = (383.40 * 6)

print('~' * 61)
print(f'{"      Olá, o total a ser pago à autoescola é de {:.2f}".format(total)}')
print('~' * 61)

totParcelas = int(input('Quantas parcelas você já pagou? '))
rest = total - (totParcelas * 383.40)
restPar = 6 - totParcelas

resp = ''
while not resp == 'SN':
    resp = str(input('Já pagou a aula online? ')).upper().strip()[0]
    if resp == 'N':
        total += 200
        break
    elif resp == 'S':
        break
print('-=' * 30)
print(f'Faltam pagar {restPar} parcelas, com total de R${rest:.2f}')
print('-=x=-' * 12)

banco = float(input('Quanto você tem no banco agora? '))
devem = float(input('Quanto te devem? '))
print('-=x=-' * 12)

saldo = (banco + devem) - rest
print(f'Você possuí um saldo de {saldo:.2f} para aproveitar sem trabalhar!')