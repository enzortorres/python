def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando fazer uma divisão por 0!')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float.\n'
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

def divide(n, d):
    
    deve_ser_int_ou_float(d)
    deve_ser_int_ou_float(n)
    nao_aceito_zero(d)
    return n / d

print(divide('enzo',0))