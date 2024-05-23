#Desenvolva um programa que leia o comprimento de três retas e diga o usuário se elas podem ou nao formar um triângulo.
r1 = float(input('\033[4;33mPrimeiro segmento: '))
r2 = float(input('\033[4;33mSegundo segmento: '))
r3 = float(input('\033[4;33mTerceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('\033[0;32mOs segmentos acima podem formar triângulos!')
else:
    print('\033[0;31mOs segmentos acima não podem formar triângulos!')
    