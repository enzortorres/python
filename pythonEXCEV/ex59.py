from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
menu = 0
while menu != 7:
    menu = int(input('''Temos essas opções: 
    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Divisão
    [5] Maior número
    [6] Novos números
    [7] Sair do progama
    >>>> Deseja realizar qual operação? '''))
    if menu == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('{} - {} = {}'.format(n1, n2, n1 - n2))
    elif menu == 3:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif menu == 4:
        print('{} / {} = {}'.format(n1, n2, n1 / n2))
    elif menu == 5:
        if n1 > n2:
            print('{} é maior do que {}!'.format(n1, n2))
        else:
            print('{} é maior do que {}!'.format(n2, n1))
    elif menu == 6:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif menu == 7:
        print('Desligando programa em')
        print('3...')
        sleep(1)
        print('2...')
        sleep(1)
        print('1...')
        sleep(1)
        print('Programa desligado! Volte sempre!')
    else:
        print('Opção inválida! Tente novamente!')
    print('=-='*15)
    sleep(1.5)