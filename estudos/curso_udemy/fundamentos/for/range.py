"""
    for + range
    range(start, stop, step), caso coloque somente um número, ele será o stop.
    Iterável -> str, range, etc (__iter__)
    Iterador -> quem sabe entregar um valor por vez
    next -> me entregue o próximo valor
    iter -> me entregue seu iterador
"""
numeros = range(10) # ? numeros de 0 a 9, se colocar somente um número, será o stop
numeros = range(5, 10) # ? numeros de 5 a 9
numeros = range(5, 10, 2) # ? numeros de 5 a 9, pulando de 2 em 2

numeros = range(10, 0, -1) # ? numeros de 10 a 1, se o step for negativo, precisa inverter os valores do start com o stop

for numero in numeros:
    print(numero)
    
print('\n' + '=' * 30 + '\n')

texto = iter('Enzo') # 'Enzo'.__iter__()

print(texto)
print(next(texto)) # texto.__next__()
print(next(texto)) # texto.__next__()
print(next(texto)) # texto.__next__()
print(next(texto)) # texto.__next__()
