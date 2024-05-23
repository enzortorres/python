
def leiaInt(msg):
    """
    -> Função para analisar um número inteiro.
    :param msg: Lê o valor digitado.
    :return: O valor em forma de n.
    Função criada por Enzo Ribas Torres.
    """
    
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[32mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    """
    -> Função para analisar um número real.
    :param msg: Lê o valor digitado.
    :return: O valor em forma de n.
    Função criada por Enzo Ribas Torres.
    """

    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[32mERRO! Por favor, digite um número real válido.\033[m')
            continue
        else:
            return n
