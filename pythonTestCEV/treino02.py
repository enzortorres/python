list = []
total = 1

while True:
    list.append(str(input('Quem deseja adicionar na lista? ')))
    total += 1
    resp = ' '
    if total == 16:
        break
print(f'''O total de pessoas que estão na lista é de {len(list)} pessoas.
{"-="*40}''')
for pessoa in list:
    print(pessoa)
    if total == 15:
        print()
print('-='*40)
