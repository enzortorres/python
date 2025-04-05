import os, json

def criarArquivo(file_path):
    infos = {
        'tarefas': [],
        'tarefas_desfeitas': [],
    }
    
    with open(file_path, "w", encoding="UTF-8") as file:
        json.dump(infos, file, ensure_ascii=False, indent=4)
    print("JSON criado!")
    
def lerArquivo(file_path):
    infos = []
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            infos = json.load(file)
    except FileNotFoundError:
        print("Arquivo não existe!")
    return infos

def salvarDados(dados, file_path):
    with open(file_path, "w") as file:
        json.dump(
            dados,
            file,
            ensure_ascii=False,
            indent=4
        )

def exibir_tarefas(file_path):
    infos = lerArquivo(file_path)

    print(f"\nTAREFAS:")
    if not infos['tarefas']:
        print("Nenhuma tarefa a realizar")
        return
    for i, item in enumerate(infos['tarefas'], start=1):
        print(f"{i}: {item}")

def desfazer(file_path):
    infos = lerArquivo(file_path)
    
    if not infos['tarefas']:
        print("\nNenhuma tarefa para desfazer!")
        return 
    
    infos['tarefas_desfeitas'].append(infos['tarefas'].pop())
    print(f"\nDesfiz a tarefa {infos['tarefas_desfeitas'][-1]}")
    
    salvarDados(infos, file_path)
    exibir_tarefas(file_path)

def refazer(file_path):
    infos = lerArquivo(file_path)

    if not infos['tarefas_desfeitas']:
        print("\nNenhuma tarefa para refazer!")
        return
    
    infos['tarefas'].append(infos['tarefas_desfeitas'].pop())
        
    salvarDados(infos, file_path)
    exibir_tarefas(file_path)


def adicionar(tarefa, file_path):
    tarefa = tarefa.strip()
    if not tarefa:
        print("\nVocê não digitou nenhuma tarefa!")
        return
    
    infos = lerArquivo(file_path)
        
    infos['tarefas'].append(tarefa)
    infos['tarefas_desfeitas'].clear()
        
    salvarDados(infos, file_path)
    print(f'\n{tarefa=} adicionada na lista de tarefas!')
    exibir_tarefas(file_path)

caminho_arquivo = 'C:\\Users\\enzor\\OneDrive\\Desktop\\Estudos\\python\\estudos\\curso_udemy\\exercicios\\'
file_path = caminho_arquivo + 'ex23.json'

if not os.path.exists(file_path):
    criarArquivo(file_path)
while True:
    print("\nComandos: listar, desfazer, refazer, clear")
    tarefa = input("Digite uma tarefa ou comando: ").strip()
    
    comandos = {
        'listar': lambda: exibir_tarefas(file_path),
        'refazer': lambda: refazer(file_path),
        'desfazer': lambda: desfazer(file_path),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, file_path),
    }
    
    if tarefa in comandos:
        comandos[tarefa]()
    elif tarefa == 'sair':
        print("Saindo do sistema...")
        break
    else:
        adicionar(tarefa, file_path)
