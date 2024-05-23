soma = 0 
cont = 0
for c in range(1, 7):
    valor = int(input('Digite o {}º valor: '.format(c)))
    if valor % 2 == 0:
        soma += valor
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))
