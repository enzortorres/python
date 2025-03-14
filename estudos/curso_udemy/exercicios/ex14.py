def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
        print(str(numero), " x " if numero != args[-1] else " = ", end='', sep='')
    print(total)
    
multiplicar(1,2,3,4)