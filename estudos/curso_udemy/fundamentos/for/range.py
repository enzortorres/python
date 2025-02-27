"""
    :
    :
    :
"""
numeros = range(10) # ? numeros de 0 a 9, se colocar somente um número, será o stop
numeros = range(5, 10) # ? numeros de 5 a 9
numeros = range(5, 10, 2) # ? numeros de 5 a 9, pulando de 2 em 2

numeros = range(10, 0, -1) # ? numeros de 10 a 1, se o step for negativo, precisa inverter os valores do start com o stop

for numero in numeros:
    print(numero)