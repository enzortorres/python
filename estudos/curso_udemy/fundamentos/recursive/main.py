"""
    | Funções recursivas e recursividade
    ? funções que podem se chamar de volta
    ? úteis p/ dividir problemas grandes em partes menores
    
    > Toda função recursiva deve ter:
    ? Um problema que possa ser dividido em partes menores
    ? Um caso recursivo que resolve o pequeno problema
    ? Um caso base que para a recursão
    
    ? fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
    ? https://brasilescola.uol.com.br/matematica/fatorial.htm
""" 
# import sys
# sys.setrecursionlimit(1004) # > Para aumentar o limite de recursão

# def recursiva(inicio=0, fim=10):
#     # ! Caso base
#     if inicio >= fim:
#         return fim
    
#     print(inicio, fim)
    
#     # ! Caso recursivo
#     # ? Conta até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(6))