
# #! EXERCÍCIO 1
# idade = float(input("Digite sua idade: "))

# if 18 <= idade <= 70:
#     print("Pode votar!")
# else:
#     print("Não pode votar!")



# #! EXERCÍCIO 2

# def soma(n1, n2):
#     return n1 + n2

# def sub(n1, n2):
#     return n1 - n2

# def mult(n1, n2):
#     return n1 * n2

# def div(n1, n2):
#     if(n1 == 0 or n2 == 0):
#         print("\n\033[1;31mNão se pode realizar divisão por 0!\033[0m\n")
#         exit()
#     else:
#         return n1 / n2

# oper = int(input('''Qual operação de seja realizar?
# Soma (1)
# Subtração (2)
# Multiplicação (3)
# Divisão (4)
# >>>'''))

# if oper not in (1,2,3,4):
#     print("Operação invalida! Tente novamente!")
#     exit()

# n1 = float(input("Digite o primeiro valor: "))
# n2 = float(input("Digite o segundo valor: "))

# if oper == 1:
#     result = soma(n1, n2)
# elif oper == 2:
#     result = sub(n1, n2)
# elif oper == 3:
#     result = mult(n1, n2)
# elif oper == 4:
#     result = div(n1, n2)

# print(f"O resultado da operação é: {result}")



#! EXERCÍCIO 3
prev_salario = float(input("Digite o salario: "))
curr_salario = 0

if prev_salario <= 280:
    aumento = 20
    curr_salario = prev_salario + prev_salario * (aumento / 100)
elif prev_salario <= 700:
    aumento = 15
    curr_salario += prev_salario + prev_salario * (aumento / 100)
elif prev_salario <= 1500:
    aumento = 10
    curr_salario += prev_salario + prev_salario * (aumento / 100)
else:
    aumento = 5
    curr_salario += prev_salario + prev_salario * (aumento / 100)

print(f"O salario de R${prev_salario:.2f} passou a ser R${curr_salario:.2f} com um aumento de {aumento}%!".replace(".", ","))