from math import hypot
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hypo = hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hypo:.2f}')
