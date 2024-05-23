from random import choice
from time import sleep
print('\033[0;35m-=x\033[m'*20)
print('\033[0;33m{:-^74}'.format('\033[4;33mJokenpô\033[0;33m'))
print('\033[0;35m-=x\033[m'*20)
lista = ['Pedra', 'Papel', 'Tesoura']
escolhido = choice(lista)

jogada = str(input('\033[0;33mQual a sua jogada? \033[0;30m'))
jogada = jogada.lower()
jogada = jogada.capitalize()
print('\033[0;31mJO!')
sleep(1)
print('\033[0;32mKEN!')
sleep(1)
print('\033[0;33mPÔ!!!')
if jogada == escolhido:
    print('\033[0;36m{} com {}!\033[0;35m Empate!\033[m'.format(jogada,
                                        escolhido))
elif jogada == 'Pedra' and escolhido == 'Papel':
    print('\033[0;36mPedra com Papel!\033[0;31m Você perdeu! Tente novamente!\033[m')
elif jogada == 'Pedra' and escolhido == 'Tesoura':
    print('\033[0;36mPedra com Tesoura!\033[0;32m Parabéns, você ganhou!\033[m')
elif jogada == 'Papel' and escolhido == 'Pedra':
    print('\033[0;36mPapel com Pedra!\033[0;32m Parabéns, você ganhou!\033[m')
elif jogada == 'Papel' and escolhido == 'Tesoura':
    print('\033[0;36mPapel com Tesoura!\033[0;31m Você perdeu! Tente novamente!\033[m')
elif jogada == 'Tesoura' and escolhido == 'Pedra':
    print('\033[0;36mTesoura com Pedra!\033[0;31m Você perdeu! Tente novamente\033[m')
elif jogada == 'Tesoura' and escolhido == 'Papel':
    print('\033[0;36mTesoura com Papel!\033[0;32m Parabéns, você ganhou!\033[m')
else:
    print('\033[1;4;31mJogada Inválida! Tente outra!')