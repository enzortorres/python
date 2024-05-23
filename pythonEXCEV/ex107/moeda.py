def metade(preco):
    """
    -> Função para mostrar a metade de um valor.
    :param preco: Preço do produto.
    :return: Retorna a metade do valor.
    Função criada por Enzo Ribas Torres
    """
    res = preco / 2
    return res


def dobro(preco):
    """
    -> Função para mostrar o dobro de um valor.
    :param preco: Preço do produto.
    :return: Retorna o dobro do valor.
    Função criada por Enzo Ribas Torres
    """
    res = preco * 2
    return res


def aumentar(preco, taxa):
    """
    -> Função para mostrar o aumento de uma taxa em cima de um valor.
    :param preco: Preço do produto.
    :param taxa: Taxa da qual deseja aumentar.
    :return: Retorna o valor com aumento da taxa.
    Função criada por Enzo Ribas Torres
    """
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco, taxa):
    """
    -> Função para mostrar a redução de uma taxa em cima de um valor.
    :param preco: Preço do produto.
    :param taxa: Taxa da qual deseja reduzir.
    :return: Retorna o valor com redução da taxa.
    Função criada por Enzo Ribas Torres
    """
    res = preco - (preco * taxa/100)
    return res

