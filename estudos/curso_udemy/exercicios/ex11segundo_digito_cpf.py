"""
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

cpf = str(input('Digite seu CPF: ')).replace('.', '').replace('-','') # ! pegar como str, para caso comece com '0', se for int, vai cortar o primeiro digito
tamanho = len(cpf)

try:
    if tamanho == 11:
        soma = 0
        cpf_digitos = cpf[0:10].__iter__()

        for i in range(11, 1, -1):
            soma += (i * int(next(cpf_digitos)))

        resultado = soma * 10
        segundo_digito = resultado % 11
        segundo_digito = 0 if segundo_digito >= 10 else segundo_digito

        print(f"Segundo digito calculado: {segundo_digito}")
        print(f"Segundo digito: {cpf[10]}")
        print('Segundo digito válido!' if segundo_digito == int(cpf[10]) else 'Segundo digito inválido')
    else:
        raise ValueError("CPF inválido, o número de dígitos deve ser 11.")
    
except Exception as error:
    print(f"Digite um cpf válido. ERRO: \033[31m{error}\033[m")