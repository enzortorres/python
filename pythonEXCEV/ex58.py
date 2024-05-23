from random import randint
computador = randint(0, 10)
resposta = 9999
c = 99999
print('\033[35m='*50)
print('''\033[33m Desafio contra máquina!!!
    \033[36mAcabei de pensar em um número entre 0 e 10.
    Será que você consegue adivinhar qual foi? ''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\033[34mQual é o seu palpite?\033[30m '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[31mMais... Tente mais uma vez!')
        elif jogador > computador:
            print('\033[31mMenos... Tente mais uma vez!')
print('\033[32mVocê acertou em \033[4;30m{}\033[0;32m palpites! Meus parabéns!\033[m'.format(palpites))
print('\033[35m=\033[m'*50)
