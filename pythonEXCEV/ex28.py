from random import choice
lista = [1, 2, 3, 4, 5]
escolhido = choice(lista)
num = int(input('Escolha um número: '))
if num == escolhido:
    print('Parabéns, vc acertou!')
else:
    print('Você errou! Tente novamente! RESULTADO: {}'.format(escolhido))
