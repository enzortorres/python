from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range(1 , 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
print('E também tivemos {} pessoas menores de idade'.format(totalmenor))

