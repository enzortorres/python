#Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final mostre os 10 primeiros termos dessa progressao.
primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(' {}'.format(c), end=' ➝ ')
print('ACABOU')
