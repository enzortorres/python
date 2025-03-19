# ? Função - def nome():

def linha(tam = 42):
    print('-' * tam)
    
linha() # linha com tamanho padrão (42)
linha(50) # Linha com tamanho de 50

# ? -------------------------------------------

def mostrar_nome(nome):
    print(f"Boa noite! {nome}!")

qtd_nome  = int(input("Digite a quantidade de pessoas: "))

for i in range(qtd_nome):
    mostrar_nome(input("Digite o seu nome: "))

def soma(a, b):
    s = a + b 
    return f"A soma de {a} + {b} = {s}"

print(soma(1,2))

# ? --------------------------------------------

def exemplo(**kwargs):
    print(kwargs)
    
exemplo(nome='Enzo', sobrenome='Ribas', idade=20)

# ? --------------------------------------

try:
    num = int(input("Digite um número: "))
    print(num)
except ValueError:
    print(f"Digite somente números!")
except KeyboardInterrupt:
    print(f"ERRO! Teclado interrompido")