primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ➝  '.format(termo), end ='')
    termo += razao
    cont += 1
print('FIM')