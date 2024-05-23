def ficha(jog='<desconhecido>', gol=0):
    """
    :param jog: Nome do jogador.
    :param gol: Quantidade gols.
    :return: Retorna o nome do jogador com n e a quantidade de gols com g.
    Função criada por Enzo Ribas Torres.
    """
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)