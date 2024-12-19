from random import randint 
from time import sleep

def linha():
    print('\033[33m-=-\033[m'*25)

while True:
    resp = ' '
    while  not resp in 'SN':
        resp = str(input('\033[36mVocê está pronto? \033[37m[\033[32mS\033[37m/\033[31mN\033[37m] ')).upper().strip()[0]
        if resp == 'S':
            sleep(1)
            print('\033[32mEntão vamos começar os jogos!\033[m')
        elif resp == 'N':
            sleep(0.6)
            print('\033[31mVolte quando estiver pronto!\033[m')
            sleep(0.3)
            exit()
            
    linha()
    escolha = str(input('''\033[32mEASY \033[37m[ 1 ]
\033[33mNORMAL \033[37m[ 2 ]
\033[30mHARD \033[37m[ 3 ]
\033[31mNIGHTMARE \033[37m[ 4 ]
\033[35mEscolha uma dificuldade:\033[30m '''))
    linha()
    easy = '1' in escolha
    normal = '2' in escolha
    hard = '3' in escolha
    nightmare = '4' in escolha
    tentativas = 0

    if easy == True:
        print('\033[37mNível fácil? Patético!\033[m')
        while True:
            tentativas += 1
            computador = randint(0,3)
            linha()
            jogador = int(input('\033[36mSortiei um número de 0 a 3, tente acertar! \033[m'))
            linha()
            if computador == jogador:
                if tentativas == 1:
                    print('\033[32mParabéns! Você acertou de primeira! Mas estava no modo fácil, então não se gabe!\033[m')
                    break
                else:
                    print(f'\033[32mParabéns! Você acertou com {tentativas} tentativas!\033[m')
                    break
            else:
                print(f'\033[1;31mCOMO PODE ERRAR NO MODO EASY?!\033[0;31m O número era {computador}! Tente novamente!\033[m')
                tentar = ' '
                while not tentar in "SN":
                    tentar = str(input('\033[36mVocê deseja continuar? \033[37m[\033[32mS\033[37m/\033[31mN\033[37m] \033[30m')).upper().strip()[0]
                if tentar == 'N':
                    linha()
                    print('\033[1;31mSÉRIO?!! DESISTIR NO MODO EASY? VOCÊ É UM FRACO!\033[0m')
                    linha()
                    break
        continuar = ' '
        while not continuar in 'SN':
            continuar = str(input('\033[36mVocê deseja continuar? \033[37m[\033[32mS\033[37m/\033[31mN\033[37m] \033[30m')).upper().strip()[0]
            if continuar == 'S':
                linha()
            else:
                exit()

    if normal == True:
        while True:
            tentativas += 1
            computador = randint(0,5)
            jogador = int(input('\033[36mSortiei um número de 0 a 5, tente acertar! \033[m'))
            linha()
            if computador == jogador:
                if tentativas == 1:
                    print('\033[32mParabéns! Você acertou de primeira!\033[m')
                    break
                else:
                    print(f'\033[32mParabéns! Você acertou com {tentativas} tentativas!\033[m')
                    break
            else:
                print(f'\033[31mVocê errou! Deploravél! O número era {computador}! Tente novamente!\033[m')
                tentar = ' '
                while not tentar in "SN":
                    tentar = str(input('\033[36mVocê deseja continuar? \033[37m[\033[32mS\033[37m/\033[31mN\033[37m] \033[30m')).upper().strip()[0]
                if tentar == 'N':
                    print('\033[31mDesistir é para os fracos!')
                    break
        continuar = ' '
        while not continuar in 'SN':
            continuar = str(input('\033[36mVocê deseja continuar? \033[37m[\033[32mS\033[37m/\033[31mN\033[37m] \033[30m')).upper().strip()[0]
        if continuar == 'S':
            linha()
        else:
            exit()

    if hard == True:
        print('NIVEL HARD! AS COISAS ESTÃO FICANDO DIFÍCEIS! BOA SORTE')
        while True:
            tentativas += 1
            computador = randint(0,9)
            linha()
            jogador = int(input('\033[36mSortiei um número de 0 a 9, tente acertar! \033[m'))
            linha()
            if computador == jogador:
                if tentativas == 1:
                    print('\033[32mParabéns! Você acertou de primeira no nível HARD! Você é um gênio!\033[m')
                    break
                else:
                    print(f'\033[32mParabéns! Você acertou com {tentativas} tentativas! Mas tudo bem, está no nível HARD!\033[m')
                    break
            else:
                print(f'\033[31mVocê errou! O número era {computador}! Tente novamente!\033[m')
                tentar = ' '
                while not tentar in "SN":
                    tentar = str(input('Você deseja continuar? \033[37m[\033[32mS\033[37m/\033[31mN\033[37m] \033[30m')).upper().strip()[0]
                if tentar == 'N':
                    print('\033[30mRealmente, no modo \033[31mHARD\033[30m é difícil acertar! Tente novamente mais tarde!\033[m')
                    break
        continuar = ' '
        while not continuar in 'SN':
            continuar = str(input('\033[36mVocê deseja continuar? \033[37m[\033[32mS\033[37m/\033[31mN\033[37m] \033[30m')).upper().strip()[0]
        if continuar == 'S':
            linha()
        else:
            exit()

    if nightmare == True:
        print('\033[4;31mNIVEL NIGHTMARE! AGORA EU DUVIDO VOCÊ ACERTAR! BOA SORTE, VOCÊ VAI PRECISAR!\033[0m')
        while True:
            tentativas += 1
            computador = randint(0,15)
            linha()
            jogador = int(input('\033[4;31mSortiei um número de 0 a 15, duvido acertar!\033[30m '))
            linha()
            if computador == jogador:
                if tentativas == 1:
                    print('\033[4;32mOQUE?!!! VOCÊ ACERTOU DE PRIMEIRA NO NÍVEL NIGHTMARE??! VOCÊ É UM DEUS!\033[m')
                    break
                else:
                    print(f'\033[4;32mMeus Parabéns! Você acertou com {tentativas} tentativas! Acertar no modo NIGHTMARE não é uma coisa fácil!\033[m')
                    break
            else:
                print(f'\033[0;31mVocê errou! O número era {computador}! Tente novamente!\033[m')
                tentar = ' '
                while not tentar in "SN":
                    tentar = str(input('\033[31mVocê deseja continuar? \033[37m[\033[32mS\033[37m/\033[31mN\033[37m] \033[m')).upper().strip()[0]
                if tentar == 'N':
                    print('\033[30mRealmente, no modo \033[4;31mNIGHTMARE\033[0;30m é impossível acertar, melhor desistir!')
                    break
        continuar = ' '
        while not continuar in 'SN':
            continuar = str(input('\033[36mVocê deseja continuar? \033[37m[\033[32mS\033[37m/\033[31mN\033[37m] \033[30m')).upper().strip()[0]
        if continuar == 'S':
            linha()
        else:
            exit()

