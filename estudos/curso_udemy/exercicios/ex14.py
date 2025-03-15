def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
        print(str(numero), " x " if numero != args[-1] else " = ", end='', sep='')
    print(total)
    
multiplicar(1,2,3,4)


def par_impar(number):
    try:
        if number % 2 == 0:
            return f"{number} é par."
        return f"{number} é ímpar."
    except:
        return("Digite apenas números.")


print(par_impar(3))