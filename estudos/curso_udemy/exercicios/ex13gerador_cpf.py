from random import randint
from re import sub

def linha(tam = 42):
    print('\n' + "=" * tam + '\n')
    
cpf_string = ''

for i in range(9):
    cpf_string += str(randint(0,9))

cpf = sub(r'[^0-9]', '', cpf_string) 

linha()
try:
        # ? Cálculo para descobrir o primeiro dígito

        soma_primeiro_digito = 0
        cpf_digitos_primeiro_digito = cpf[0:9].__iter__()
        for i in range(10, 1, -1):
            soma_primeiro_digito += (i * int(next(cpf_digitos_primeiro_digito)))

        resultado_primeiro_digito = (soma_primeiro_digito * 10) % 11
        primeiro_digito = 0 if resultado_primeiro_digito >= 10 else resultado_primeiro_digito
        
        cpf += str(primeiro_digito)
        
        # ? Cálculo para descobrir o segundo dígito
        
        soma_segundo_digito = 0
        cpf_digitos_segundo_digito = cpf[0:10].__iter__()
        for i in range(11, 1, -1):
            soma_segundo_digito += (i * int(next(cpf_digitos_segundo_digito)))
        
        resultado_segundo_digito = (soma_segundo_digito * 10) % 11
        segundo_digito = 0 if resultado_segundo_digito >= 10 else resultado_segundo_digito
        
        cpf += str(segundo_digito)
        
        cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        print(f'CPF válido gerado: {cpf_formatado}')  
        
except Exception as error:
    print(f"Erro ao gerar CPF: \033[31m{error}\033[m")
linha()