nome = str(input("Digite seu nome: "))
index = 0
novo_nome = ''

while index < len(nome):
    novo_nome += '*' + nome[index] 
    index += 1


print(nome, novo_nome)