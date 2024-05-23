jogador = {'nome':'','partidas':0,'gols':0,'total':0}
jogos = []

jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Quantas partidas jogou: '))

for p in range(0, jogador['partidas']):
    partidas = int(input(f'Quantos gols na {p+1}ª partida? '))
    jogador['total'] += partidas
    jogos.append(partidas)
jogador['gols'] = jogos

print('-=' * 20)

for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}.')

print('-=' * 20)

print(f'O Jogador {jogador["nome"]} jogou 5 partidas')
for p, g in enumerate(jogador['gols']):
    print(f'Na partida {p+1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]}')
