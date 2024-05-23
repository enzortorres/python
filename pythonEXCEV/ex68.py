from random import randint
n = cont = 0
resultado = ''
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    computador = randint(0, 10)
    n = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    total = n + computador
    print('-'*40)
    if total % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'    
    print(f'Você jogou {n} e o computador {computador}. Total de {total}', end=' ')
    if resultado == 'P':
        print('DEU PAR')
    else:
        print('DEU IMPAR')
    if resultado == escolha:
        print('''Você GANHOU
Vamos jogar novamente...''')
        cont += 1
    else:
        break
print('=-'*20)
print(f'GAME OVER! Você venceu {cont} vezes.')    