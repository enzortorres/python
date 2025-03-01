import os

def mostrar_lista(lista):
    os.system('cls')
    print("." * 30)
    print(f"{'LISTA DE COMPRAS': ^30}") # ? (: ^30) serve para centralizar a string/variável para o meio em 30 espaços.
    for itens in enumerate(lista, start=1):
        i, item = itens
        print(f'{i} - {item: >26}')
    print("." * 30)

def add_item(lista, item):
    lista.append(item)

def remove_item(lista, item):
    lista.remove(item)

lista = []

while True:
    opcao = 0
    try:
        opcao = int(input("""\nSelecione uma opção:
[1] Adicionar item
[2] Remover item
[3] Mostrar lista
>>> """))
    except:
        print("\n\033[31mDigite um valor válido.\033[m\n")
        continue

    if opcao == 1:
        os.system('cls')
        item = str(input("Digite o item que deseja adicionar: "))
        add_item(lista, item)
        print(f"\n\033[32m{item} adicionado com sucesso.\033[m\n")

    elif opcao == 2:
        try:
            os.system('cls')
            item_remover = str(input("Que item deseja remover? "))
            item_index = lista.index(item_remover)
            print(f'\n\033[32m{item_remover} removido com sucesso da lista.\033[m\n')
            remove_item(lista, item)
            
        except Exception as error:
            print(f'\n\033[31mO item {item_remover} não existe na lista.\033[m\n')
    
    elif opcao == 3:
        mostrar_lista(lista)

    else:
        print("\n\033[31mDigite um valor válido.\033[m\n")
        continue
    
    resp = ' '
    while resp not in "sim||nao||não":
        resp = str(input("Deseja continuar? (sim/não) ")).lower()
        os.system('cls')
        if resp in 'não||nao':
            print("\n\033[31mEncerrando programa...\033[m\n")
            exit()