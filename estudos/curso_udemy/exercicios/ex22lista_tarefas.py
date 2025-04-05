import os

tarefas = []
tarefas_desfeitas = []

def exibir_tarefas(lista):
    print(f"\nTAREFAS:")
    if lista:
        for item in lista:
            print(item)
        return
    print("Nenhuma tarefa a realizar")

def desfazer(tarefas, tarefas_desfeitas):
    if tarefas:
        tarefas_desfeitas.append(tarefas.pop())
        print(f"\nDesfiz a tarefa {tarefas_desfeitas[-1]}!")
        return 
    print("\nNenhuma tarefa para desfazer!")
    exibir_tarefas(tarefas)
    
def refazer(tarefas, tarefas_desfeitas):
    if tarefas_desfeitas:
        tarefas.append(tarefas_desfeitas[-1])
        tarefas_desfeitas.pop()
        return
    print("\nNenhuma tarefa para refazer!")
    exibir_tarefas(tarefas)
    
def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print("\nVocê não digitou nenhuma tarefa!")
    tarefas.append(tarefa)
    
    print(f'\n{tarefa=} adicionada na lista de tarefas!')
    exibir_tarefas(tarefas)

while True:
    print("\nComandos: listar, desfazer, refazer")
    comando = input("Digite uma tarefa ou comando: ")
    
    if comando == 'listar':
        exibir_tarefas(tarefas)
        continue

    elif comando == 'desfazer':
        desfazer(tarefas, tarefas_desfeitas)
        continue

    elif comando == 'refazer':
        refazer(tarefas, tarefas_desfeitas)
        continue

    elif comando == 'sair':
        print("\nSaindo do sistema...")
        break

    elif comando == 'clear':
        os.system('cls')
        continue
    else:
        adicionar(comando, tarefas)