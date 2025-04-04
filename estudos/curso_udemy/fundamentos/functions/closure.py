"""
    Closure e funções que retornam oturas funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Enzo'))
print(falar_boa_noite('Enzo'))

for nome in ['Roxie', 'Alvin', 'Ella']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))


def multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(5))
print(triplo(5))