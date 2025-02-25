# # ! EXERCÍCIO 1
# number = int(input("Digite um número: "))
# if number < 0:
#     print("Digitou um número negativo.")
# elif number == 0:
#     print("Digitou o número 0.")
# else:
#     print("Digitou um número positivo.")



# # ! EXERCÍCIO 2
# notas = []
# soma = 0

# for nota in range(0,3):
#     nota = float(input("Digite uma nota: ")) 
#     soma += nota

# media = soma / 3
# if media < 5:
#     print("Reprovado.")
# elif media < 7:
#     print("Recuperação.")
# else: 
#     print("Aprovado.")



# # ! EXERCÍCIO 3
# number1 = int(input("Digite um numero: "))
# number2 = int(input("Digite outro numero: "))

# if number1 % number2 == 0:
#     print(f'O número {number1} é multiplo do número {number2}.')
# else:
#     print(f'O número {number1} não é multiplo do número {number2}.')



# # ! EXERCÍCIO 4
# numbers = []
# ordem_correta = False
# for i in range(3):
#     number = float(input(f"Digite o {i+1} número: "))
#     numbers.append(number)

# if numbers == sorted(numbers):
#     print('Os números estão em ordem crescente!')
# else:
#     print('Os números não estão em ordem crescente!')



# # ! EXERCÍCIO 5
# number = int(input("Digite um número: "))

# def contarImpares(number):
#     qtd_impares = 0
#     for i in range(1, number + 1):
#         if i % 2 != 0: qtd_impares += 1
#     return qtd_impares

# qtd_impares = contarImpares(number)
# print(f'Quantidade de ímpares existentes entre 1 e {number}: {qtd_impares}')



# # ! EXERCÍCIO 6
# number = int(input("Digite um número para ver seu fatorial: "))

# def fat(n):
#     fat = 1
#     for i in range(n):
#         fat *= n - i
#     return fat

# print(f'O fatorial de {number} é {fat(number)}.')



# # ! EXERCÍCIO 7

# def contarDigitos(number):
#     return len(str(abs(number)))
# number = int(input("Digite um número: "))
# qtd_digitos = contarDigitos(number)

# print(f'O número {number} possuí {qtd_digitos} digitos.')



# # ! EXERCÍCIO 8
# def isNumeroPerfeito(number):
#     soma_divisores = 0
#     for i in range(1, number):
#         if number % i == 0: soma_divisores += i
#     return soma_divisores == number

# number = int(input("Digite um número para ver se é um número perfeito: "))

# if isNumeroPerfeito(number):
#     print(f'O número {number} é um número perfeito.')
# else:
#     print(f'O número {number} não é um número perfeito.')



# # ! EXERCÍCIO 9

# def fibonacci(n):
#     if n < 1:
#         return 'Número inválido! Escolha um número maior ou igual a 1'
#     sequencia = [0, 1]
#     for i in range(0, n - 2):
#         sequencia.append(sequencia[i] + sequencia[i + 1])
#     return sequencia    
# print(fibonacci(10))



# # ! EXERCÍCIO 10
# def tabuada(base, limite):
#     for i in range(1, limite + 1):
#         print(f'{base} x {i} = {base * i}')
# tabuada(5, 7)