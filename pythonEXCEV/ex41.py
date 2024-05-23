from datetime import date
anoatual = date.today().year
ano = int(input('\033[0;33mEm que ano este atleta nasceu? \033[0;30m'))
idade = anoatual - ano
if idade < 9:
    print('\033[0;33mEste atleta está na categoria \033[4;33mMIRIM\033[m')
elif idade >= 9 and idade < 14:
    print('\033[0;33mEste atleta está na categoria \033[4;33mINFANTIL\033[m')
elif idade >= 14 and idade < 19:
    print('\033[0;33mEste atleta está na categoria \033[4;33mJUNIOR\033[m')
elif idade >= 19 and idade < 20:
    print('\033[0;33mEste atletla está na categoria \033[4;33mSÊNIOR\033[m')
elif idade > 20:
    print('\033[0;33mEste atleta está na categoria \033[4;33mMASTER\033[m')
