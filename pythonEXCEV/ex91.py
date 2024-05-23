from random import randint
from time import sleep
from operator import itemgetter

ranking = list()
jogadores = {'jogador1':randint(1, 6),
             'jogador2':randint(1, 6),
             'jogador3':randint(1, 6),
             'jogador4':randint(1, 6)}

print('-=' * 20)
print(f'{"<< VALORES SORTEADOS >>":^40}')
for k, v in jogadores.items():
     print(f'     - O {k} tirou {v} no dado.')
     sleep(1)
print('-=' * 20)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{"== RANKING DOS JOGADORES ==":^40}')
for index, valor in enumerate(ranking):
     print(f'     - O {index+1}º lugar: {valor[0]} com {valor[1]}.')
     sleep(1)