import os

# ! Exemplo 1
# > Utilizando o método Guard Clause (Tentar no máximo evitar condições)

def exibir_tarefas(lista):
    print(f"\nTAREFAS:")
    if not lista:
        print("Nenhuma tarefa a realizar")
        return
    for item in lista:
        print(item)

def desfazer(tarefas, tarefas_desfeitas):
    if not tarefas:
        print("\nNenhuma tarefa para desfazer!")
        return 
    tarefas_desfeitas.append(tarefas.pop())
    print(f"\nDesfiz a tarefa {tarefas_desfeitas[-1]}!")
    exibir_tarefas(tarefas)
        
    
def refazer(tarefas, tarefas_desfeitas):
    if not tarefas_desfeitas:
        print("\nNenhuma tarefa para refazer!")
        return
    tarefas.append(tarefas_desfeitas[-1])
    tarefas_desfeitas.pop()
    exibir_tarefas(tarefas)
    
def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print("\nVocê não digitou nenhuma tarefa!")
        return
    
    tarefas.append(tarefa)
    print(f'\n{tarefa=} adicionada na lista de tarefas!')
    exibir_tarefas(tarefas)
    
tarefas = []
tarefas_desfeitas = []

while True:
    print("\nComandos: listar, desfazer, refazer")
    tarefa = input("Digite uma tarefa ou comando: ") 
    
    comandos = {
        'listar': lambda: exibir_tarefas(tarefas),
        'refazer': lambda: refazer(tarefas, tarefas_desfeitas),
        'desfazer': lambda: desfazer(tarefas, tarefas_desfeitas),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    
    comando = comandos[tarefa.get()] if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()

# ! Exemplo 2
# > Utilizando condições 

# while True:
#     print("\nComandos: listar, desfazer, refazer")
#     comando = input("Digite uma tarefa ou comando: ")
    
#     if comando == 'listar':
#         exibir_tarefas(tarefas)
#         continue

#     elif comando == 'desfazer':
#         desfazer(tarefas, tarefas_desfeitas)
#         continue

#     elif comando == 'refazer':
#         refazer(tarefas, tarefas_desfeitas)
#         continue

#     elif comando == 'sair':
#         print("\nSaindo do sistema...")
#         break

#     elif comando == 'clear':
#         os.system('cls')
#         continue
#     else:
#         adicionar(comando, tarefas)