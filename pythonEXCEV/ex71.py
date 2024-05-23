print('='*20)
print('{:^20}'.format('BANCO MF'))
print('='*20)
saque = int(input('Digite o valor que deseja sacar: '))
ced = 50
totalced = 0
total = saque
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('='*30)
print('{:^30}'.format('Volte sempre ao BANCO DO MUDINHO! Tenha um bom dia!'))