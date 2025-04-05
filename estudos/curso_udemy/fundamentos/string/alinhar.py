import os
lista = ['Arroz', 'Feijão', 'Água']

def mostrar_lista(lista):
    os.system('cls')
    print("." * 30)
    print(f"{'LISTA DE COMPRAS': ^30}") # ? (: ^30) serve para centralizar a string/variável para o meio em 30 espaços.
    for itens in enumerate(lista, start=1):
        i, item = itens
        print(f'{i} - {item: >26}') # ? (: >26) server para alinhar a string/variável para a direita em 26 espaços. (:.>26) para preencher com "." no lugar do espaço
    print("." * 30)
    
mostrar_lista(lista)