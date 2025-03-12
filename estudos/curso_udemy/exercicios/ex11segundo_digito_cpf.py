cpf = str(input('Digite seu CPF: ')) # ! pegar como str, para caso comece com '0', se for int, vai cortar o primeiro digito

try:
    soma = 0
    cpf = cpf.replace('.', '').replace('-','')
    print(cpf)
    cpf_digitos = cpf[0:10].__iter__()
    
    for i in range(11, 1, -1):
        soma += (i * int(next(cpf_digitos)))
        
    print(soma)
    resultado = soma * 10
    segundo_digito = resultado % 11
    segundo_digito = 0 if segundo_digito >= 10 else segundo_digito
    
    print(f"Segundo digito calculado: {segundo_digito}")
    print(f"Segundo digito: {cpf[10]}")
    print('Segundo digito válido!' if segundo_digito == int(cpf[10]) else 'Segundo digito inválido')
    
    
except Exception as error:
    print(f"Digite um cpf válido. ERRO: \033[31m{error}\033[m")