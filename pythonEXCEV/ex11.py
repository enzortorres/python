largura = float(input('\033[33mLargura da parede:\033[30m '))
altura = float(input('\033[33mAltura da parede:\033[30m '))
area = largura * altura
tinta = area / 2
print(f'''\033[34mSua parede tem a dimensão de \033[4;31m{largura}x\033[4;31m{altura}\033[0;34m e sua área é de \033[4;31m{area}m²
\033[0;34mPara pintar essa parede, você precisará de \033[4;31m{tinta}l\033[0;34m de tinta.\033[m''')
