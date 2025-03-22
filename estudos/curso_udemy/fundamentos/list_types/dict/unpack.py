a, b = 1, 2
a, b = b, a
# print(a,b)

pessoa = {
    'nome': 'Enzo',
    'sobrenome': 'Ribas'
}

dados_pessoa = {
    'idade': 20,
    'altura': 1.8,
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

# ? args e kwargs
# > args (já vimos)
# > kwargs - keyword arguments (argumentos nomeados)


mostro_argumentos_nomeados(**pessoa_completa)

configuracao = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracao)