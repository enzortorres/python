times = ('América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia',
          'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro',
            'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza',
              'Goiás', 'Grêmio', 'Internacional', 'Palmeiras',
                'Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama')
print('=-'*30)
print(f'Lista de times do Brasileirão: {times}')
print('=-'*30)
print(f'Os 5 primeiros times do Brasileirão são {times[:5]}')
print('=-'*30)
print(f'Os 4 últimos são {times[-4:]}')
print('=-'*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-'*30)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')