alunos = {}
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['media'] >= 7:
    alunos['situacao'] = 'Aprovado'
elif alunos['media'] >= 5 and alunos['media'] < 7:
    alunos['situacao'] = 'Recuperação'
elif alunos['media'] < 5:
    alunos['situacao'] = 'Reprovado'
for k, v in alunos.items():
    print(f'{k} é igual {v}')