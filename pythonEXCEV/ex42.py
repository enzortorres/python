r1 = float(input('\033[4;33mPrimeiro segmento: \033[0;30m'))
r2 = float(input('\033[4;33mSegundo segmento: \033[0;30m'))
r3 = float(input('\033[4;33mTerceiro segmento: \033[0;30m'))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('\033[0;32mOs segmentos podem formar triângulos!\033[m')
else:
    print('\033[0;31mOs segmentos não podem formar triângulos!\033[m')
if r1 == r2 and r2 != r3 or r1 != r3:
    print('\033[0;33mEste triângulo é do tipo Isósceles!')
elif r1 == r2 and r1 == r3:
    print('\033[0;33mEste triângulo é do tipo Equilátero!')
elif r1 != r2 and r1 != r3:
    print('\033[0;33mEste triângulo é do tipo Escaleno!')