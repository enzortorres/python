def voto(ano):
    """
    -> Programa que lê a sua idade e diz se o voto é obrigatório, opcional ou não vota.
    :param ano: Lê o ano em que você nasceu.
    :return   : Retorna a sua idade e a sua situação.
    Função criada por Enzo Ribas Torres.
    """
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# Programa Principal    
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
