from time import sleep

lista = []
alunos = []

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    
    media = (lista[1] + lista[2]) / 2 
    media = round(media, 1)

    lista.append(media)
    alunos.append(lista[:])
    lista.clear()
    
    resp = ' '
    while not resp in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print('-=' * 20)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>5}')
print('='*28)

for c, pessoa in enumerate(alunos):
    print(f'{c:<4}{pessoa[0]:<15}{pessoa[3]:>5}')

while True:
    print('=' * 50)
    check = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if check == 999:
        break
    print(f'Notas de {alunos[check][0]} são {alunos[check][1:3]}')
print('FINALIZANDO EM 3...', end='')
sleep(1)
print('2...',end='')
sleep(1)
print('1...')
sleep(1)
print('''SISTEMA FINALIZADO!
<<< VOLTE SEMPRE >>>''')
