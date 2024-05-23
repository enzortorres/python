def metade(preco=0, format=False):
    """
    -> Função para mostrar a metade de um valor.
    :param preco: Preço do produto.
    :param format: Se deseja que o valor seja formatado ou não.
    :return: Retorna a metade do valor.
    Função criada por Enzo Ribas Torres
    """
    res = preco / 2
    return res if format is False else moeda(res)


def dobro(preco=0, format=False):
    """
    -> Função para mostrar o dobro de um valor.
    :param preco: Preço do produto.
    :param format: Se deseja que o valor seja formatado ou não.
    :return: Retorna o dobro do valor.
    Função criada por Enzo Ribas Torres
    """
    res = preco * 2
    return res if format is False else moeda(res)


def aumentar(preco=0, taxa=0, format=False):
    """
    -> Função para mostrar o aumento de uma taxa em cima de um valor.
    :param preco: Preço do produto.
    :param taxa: Taxa da qual deseja aumentar.
    :param format: Se deseja que o valor seja formatado ou não.
    :return: Retorna o valor com aumento da taxa.
    Função criada por Enzo Ribas Torres
    """
    res = preco + (preco * taxa/100)
    return res if format is False else moeda(res)


def diminuir(preco=0, taxa=0, format=False):
    """
    -> Função para mostrar a redução de uma taxa em cima de um valor.
    :param preco: Preço do produto.
    :param taxa: Taxa da qual deseja reduzir.
    :param format: Se deseja que o valor seja formatado ou não.
    :return: Retorna o valor com redução da taxa.
    Função criada por Enzo Ribas Torres
    """
    res = preco - (preco * taxa/100)
    return res if format is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    """
    -> Função para mostrar o valor formatado.
    :param preco: Preço do produto.
    :param moeda: A formatação desejada (R$) PADRÃO
    :return: Retorna o valor formtado.
    Função criada por Enzo Ribas Torres
    """
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco=0, taxaa=10, taxar=5):
    """
    -> Função para mostrar um resumo de um valor.
    :param preco: Preço do produto.
    :param taxaa: Taxa da qual deseja aumentar em cima do valor.
    :param taxar: Taxa da qual deseja reduzir em cima do valor.
    :return: Retorna o resumo completo de um valor.
    Função criada por Enzo Ribas Torres.
    """
    print('-' * 35)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 35)
    print(f'Preço analisado: \t\t{moeda(preco)}')
    print(f'Dobro do preço: \t\t{dobro((preco), True)}')
    print(f'Metade do preço: \t\t{metade((preco), True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 35)
