frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
print('O inverso de {} é {}'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('Está frase é um políndromo!')
else:
    print('Está frase não é um políndromo!')
