from datetime import date
ano = int(input('\033[0;33mEm que ano você nasceu? \033[m'))
atual = date.today().year
idade = atual - ano
if idade == 18:
    print('\033[0;32mEstá na hora de se alistar!')
elif idade < 18:
    print('\033[0;32mAinda não está na hora de se alistar e faltam {} anos.'.format(idade - 18))
else:
    print('\033[0;30;41mJá passou o tempo de se alistar!!!\033[0;33mSe passaram {} anos desde o momento que deveria se alistar!\033[m'
          .format(idade - 18))