total18 = totalf = totalm = 0
while True:
    print('-'*30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalm += 1
    if sexo == 'F':
        if idade < 20:
            totalf += 1
    print('-'*30)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('{:=^35}'.format(' FIM DO PROGRAMA '))
print(f'''Total de pessoas com mais de 18 anos: {total18}
Ao todo temos {totalm} homens cadastrados
E temos {totalf} mulheres com menos de 20 anos''')