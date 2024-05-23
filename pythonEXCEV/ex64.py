n = int(input('\033[33mDigite um valor:\033[30m '))
total = 1
totaln = n
while n != 999:
    n = int(input('\033[33mDigite mais algum valor:\033[30m '))
    print('\033[31m[999]\033[33m Parar')
    if n != 999:
        total += 1
        totaln += n
print('''\033[34mVocê digitou \033[4m{}\033[0;34m valores no total e a soma deles é \033[4;34m{}\033[0;34m.
\033[31mSistema desligado! Volte sempre!\033[m'''.format(total, totaln))