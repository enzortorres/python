"""
    Calculo do primeiro dígito do CPF
    CPF: 746.824.890-70
    Colete a soma dos 9 primeiros dígitos do CPF
    multiplicando cada um dos valores por uma
    contagem regressiva começando de 10

    Ex.:  746.824.890-70 (746824890)
        10  9  8  7  6  5  4  3  2
        7   4  6  8  2  4  8  9  0
        70  36 48 56 12 20 32 27 0

    Somar todos os resultados: 
    70+36+48+56+12+20+32+27+0 = 301
    Multiplicar o resultado anterior por 10
    301 * 10 = 3010
    Obter o resto da divisão da conta anterior por 11
    3010 % 11 = 7
    Se o resultado anterior for maior que 9:
        resultado é 0
    contrário disso:
        resultado é o valor da conta

    O primeiro dígito do CPF é 7
    
    Calculo do segundo dígito do CPF
    
    CPF: 746.824.890-70
    Colete a soma dos 9 primeiros dígitos do CPF,
    MAIS O PRIMEIRO DIGITO,
    multiplicando cada um dos valores por uma
    contagem regressiva começando de 11

    Ex.:  746.824.890-70 (7468248907)
        11 10  9  8  7  6  5  4  3  2
        7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
        77 40 54 64 14 24 40 36  0 14

    Somar todos os resultados:
    77+40+54+64+14+24+40+36+0+14 = 363
    Multiplicar o resultado anterior por 10
    363 * 10 = 3630
    Obter o resto da divisão da conta anterior por 11
    3630 % 11 = 0
    Se o resultado anterior for maior que 9:
        resultado é 0
    contrário disso:
        resultado é o valor da conta

    O segundo dígito do CPF é 0
"""

def linha(tam = 42):
    print('\n' + "=" * tam + '\n')

linha()

import re
import random

cpf_string = str(input('Digite seu CPF: ')) # ! pegar como str, para caso comece com '0', se for int, vai cortar o primeiro digito

CPF = re.sub(r'[^0-9]', '',cpf_string)

try:
    if len(CPF) == 11 and CPF != CPF[0] * len(CPF):
        soma_primeiro_digito = 0
        soma_segundo_digito = 0
        cpf_digitos_primeiro_digito = CPF[0:9].__iter__()
        cpf_digitos_segundo_digito = CPF[0:10].__iter__()

        for i in range(10, 1, -1):
            soma_primeiro_digito += (i * int(next(cpf_digitos_primeiro_digito)))
            
        for i in range(11, 1, -1):
            soma_segundo_digito += (i * int(next(cpf_digitos_segundo_digito)))

        # ? Cálculo para descobrir o primeiro dígito
        resultado_primeiro_digito = (soma_primeiro_digito * 10) % 11
        primeiro_digito = 0 if resultado_primeiro_digito >= 10 else resultado_primeiro_digito
        
        # ? Cálculo para descobrir o segundo dígito
        resultado_segundo_digito = (soma_segundo_digito * 10) % 11
        segundo_digito = 0 if resultado_segundo_digito >= 10 else resultado_segundo_digito

        linha()
        print(f"Primeiro dígito calculado: {primeiro_digito}")
        print(f"Primeiro dígito: {CPF[9]}")
        print('Primeiro dígito válido!' if primeiro_digito == int(CPF[9]) else 'Primeiro dígito inválido')
        linha()
        print(f"Segundo dígito calculado: {segundo_digito}")
        print(f"Segundo dígito: {CPF[10]}")
        print('Segundo dígito válido!' if segundo_digito == int(CPF[10]) else 'Segundo dígito inválido')
        linha()
        
        ambos_validos = False
        if primeiro_digito == int(CPF[9]) and segundo_digito == int(CPF[10]):
            ambos_validos = True
        
        print(f'\033[32mCPF {cpf_string} é válido!\033[m' if ambos_validos else f'\033[31mCPF {cpf_string} é inválido!\033[m')
        
    elif CPF == CPF[0] * len(CPF):
        raise ValueError("\033[31mCPF inválido, o número não pode ser uma sequência de valores iguais.\033[m")
    else:
        raise ValueError("\033[31mCPF inválido, o número de dígitos deve ser 11.\033[m")
except Exception as error:
    print(f"Digite um cpf válido. ERRO: \033[31m{error}\033[m")