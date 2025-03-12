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
"""

cpf = str(input('Digite seu CPF: ')).replace('.', '').replace('-','') # ! pegar como str, para caso comece com '0', se for int, vai cortar o primeiro digito

try:
    if len(cpf) == 11:
        soma = 0
        cpf_digitos = cpf[0:9].__iter__()

        for i in range(10, 1, -1):
            soma += (i * int(next(cpf_digitos)))

        resultado = soma * 10
        primeiro_digito = resultado % 11
        primeiro_digito = 0 if primeiro_digito >= 10 else primeiro_digito

        print(f"Resultado do cálculo do primeiro digito: {resultado}")
        print(f"Primeiro digito calculado: {primeiro_digito}")
        print(f"Primeiro digito: {cpf[9]}")
        print('Primeiro digito válido!' if primeiro_digito == int(cpf[9]) else 'Primeiro digito inválido')
    else:
        raise ValueError("CPF inválido, o número de dígitos deve ser 11.")
except Exception as error:
    print(f"Digite um cpf válido. ERRO: \033[31m{error}\033[m")