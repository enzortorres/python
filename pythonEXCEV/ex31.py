dist = float(input('Qual a distância de sua viagem? '))
if dist <= 200:
    print('O preço da passagem ficou R$0.50 por km, portanto: R${}'.format(dist*0.50))
else:
    print('O preço da passagem ficou R$0.45 por km, portanto: R${}'.format(dist*0.45))