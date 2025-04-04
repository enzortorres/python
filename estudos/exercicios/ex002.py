"""
    O usuário vai digitar um número com mais de 1 digito
    Somar todos dígitos e retornar a soma
"""
def somar_digitos(number):
    number_string = str(number)
    soma = 0
    
    for c in number_string:
        soma += int(c)

    return soma

print(somar_digitos('123'))