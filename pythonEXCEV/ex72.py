numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez',
              'onze', 'doze', 'treze', 'quatorze', 'quinze',
                'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resposta = int(input('Digite um número entre 0 e 20: '))
while not resposta >= 0 or not resposta <= 20:
    resposta = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[resposta]}')
