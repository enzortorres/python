# TDE 4

# ! EXERCÍCIO 1
numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", 
    "seis", "sete", "oito", "nove", "dez", "onze", 
    "doze", "treze", "quatorze", "quinze", "dezesseis", 
    "dezessete", "dezoito", "dezenove", "vinte"
)

number = input("Digite um número para ver por extenso: ")
print(f"{number} ({numeros_por_extenso[int(number)]})")



# ! EXERCÍCIO 2
lista = []
for i in range(10):
    lista.append(int(input("Digite um número: ")))

lista_numeros_diferentes = []
for num in lista:
    if num not in lista_numeros_diferentes:
        lista_numeros_diferentes.append(num)

print(f"Essa lista possuí {len(lista_numeros_diferentes)} números diferentes")



# ! EXERCÍCIO 3
lista = []
for i in range(4):
    lista.append(int(input(f"Digite o {i+1} numero: ")))
    
pares = (n for n in lista
        if n % 2 == 0
)

print(f"Quantidade de valores 9: {lista.count(9)}")
print(f"Em que posição foi digitado o primeiro valor 3: {lista.index(3)}")
print(f"Os números pares:", *pares)



# ! EXERCÍCIO 4
from random import randint
porcentagem_dado_6 = 0
for i in range(10):
    
    lista_valores_dados = []
    for j in range(50):
        lista_valores_dados.append(randint(1,6))
    porcentagem_dado_6 += (lista_valores_dados.count(6) / 50) * 100
    
porcentagem_dado_6 /= 10
print(f"Fizemos 10 testes e a porcentagem de cair 6 ficou em média {porcentagem_dado_6:.2f}%!")



# ! EXERCÍCIO 5
tradutor = {
    'olá': 'hello',
    'mundo': 'world',
    'gato': 'cat',
    'cachorro': 'dog',
    'obrigado': 'thank you',
    'amor': 'love',
    'comida': 'food',
    'casa': 'house',
    'livro': 'book',
    'amigo': 'friend'
}

palavra = str(input("Digite uma palavra: ")).lower()
print(f"A palavra {palavra} em inglês é {tradutor[f'{palavra}']}")



# ! EXERCÍCIO 6
import os
estoque = dict()

print("Seja bem vindo ao cadastro de produtos!\n")

opcao = 0
while True:
    opcao = int(input("Oque deseja realizar?\n1 - Cadastrar produto\n2 - Ver estoque\n3 - Sair\n>>> "))
    if opcao == 1:
        os.system('cls')
        produto = str(input("Qual produto deseja cadastrar? (sair para encerrar) ")).lower()
        qtd = int(input("Digite a quantidade do produto: "))
        estoque[produto] = qtd
        print(f"{produto.capitalize()} cadastrado com sucesso!\n")
    elif opcao == 2:
        os.system('cls')
        for key, values in estoque.items():
            print(f"Produto: {key} | Quantidade: {values}")
        print()
    elif opcao == 3:
        break
print("Encerrando sistema...")



# ! EXERCÍCIO 7
idades = []
alturas = []

for i in range(5):
    idades.append(int(input(f"Digite a idade da {i+1} pessoa: ")))
    alturas.append(float(input(f"Digite a altura da {i+1} pessoa: ")))

for i in range(4, -1, -1):
    print(f"\n{i+1} pessoa:")
    print(f"Idade: {idades[i]}")
    print(f"Altura: {alturas[i]}")



# ! EXERCÍCIO 8
qtd_letras = {}

string = str(input("Digite algo: ")).lower()
for letra in string:
    qtd_letras[letra] = string.count(letra)

for key, values in qtd_letras.items():
    print(f"Letra: {key} | Qtd: {values}")



# ! EXERCÍCIO 9
def calcular_media(alunos):
    medias = {}
    soma = 0
    i = 1
    for key, values in alunos.items():
        medias[f'media_{key}'] = sum(values) / len(values)
        soma += sum(values)
        i += 1
    medias['media_geral'] = (soma / 3) / 3
    return medias

alunos = {
    "Kate": (8, 7, 6),
    "Nellie": (10, 6, 8),
    "Stephen": (5, 4, 6),
}

medias = calcular_media(alunos)
alunos.update(medias)

for k, v in alunos.items():
    print(k,v)



# ! EXERCÍCIO 10
string = input("Digite uma frase: ")

string = string.split(" ")
palavras = {}
for palavra in string:
    palavras[palavra] = string.count(palavra)
for k, v in palavras.items():
    print(f"Palavra: {k} | Qtd: {v}")



# ! EXERCÍCIO 11
def is_positive(n):
    return 'Positivo' if n > 0 else 'Negativo'

print(is_positive(5))
print(is_positive(-5))
print(is_positive(.4053))



# ! EXERCÍCIO 12

def valor_absoluto(n):
    return abs(n)

print(valor_absoluto(5))



# ! EXERCÍCIO 13
def soma(n1, n2, limite=100):
    return True if n1 + n2 <= limite else False

print(soma(50,49))
print(soma(50,100))
print(soma(10,24))



# ! EXERCÍCIO 14
def somaImposto(custo, taxaImposto):
    imposto = custo * taxaImposto / 100
    return custo + imposto
    
print(somaImposto(100,10))



# ! EXERCÍCIO 15
def qtd_digitos(num):
    num_string = str(num)
    return len(num_string)

print(qtd_digitos(100))