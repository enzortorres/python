from math import floor
n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n, floor(n)))

#Faça um progama que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. calcule e mostre o compirmento da hipotenusa
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjancente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))