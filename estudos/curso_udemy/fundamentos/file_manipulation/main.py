"""
    | Criando arquivos com Python + Context Manager with
    ? Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)
    
    > Modos:
        : r (leitura, arquivo precisa existir), w (escrita, apaga o texto anterior, cria arquivo e não le), x (somente para criação)
        : a (cria arquivo e escreve ao final, append), b (binário), t (modo texto)
        : + (leitura e escrita)
    
    > Context manager - with (abre e fecha)
    
    > Métodos úteis
        : write, read (escrever e ler)
        : writelines (escrever várias linhas)
        : seek (move o cursor)
        : readline (ler linha)
        : readlines (ler linhas)
    
    > Vamos falar mais sobre o módulo os, mas:
        : os.remove ou unlink - apaga o arquivo
        : os.rename - troca o nome ou move o arquivo
    
    > Vamos falar mais sobre o módulo json, mas:
        : json.dump = Gera um arquivo json
        : json.load
"""

import os
from pathlib import Path

# > No windows é bom usar '\\' para separar as pastas
caminho_arquivo = Path(__file__).parent
caminho_arquivo = caminho_arquivo / 'file.txt'

# > Sem with open
# try: 
#     arquivo = open(caminho_arquivo, 'r')
# except FileNotFoundError:
#     print("Arquivo não existe")
#     arquivo = open(caminho_arquivo, 'w')
#     print("Arquivo criado com sucesso!")
# finally:
#     arquivo.close()

# > Com with open, ele abre o arquivo e fecha sozinho no final
with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo: # > Para inserir caracteres especiais, utilizar encoding='utf-8'
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines( # : Para escrever quando estiver usando um iterável
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0) # : Para voltar para a primeira linha
    print(arquivo.read()) # : Para ler o arquivo todo
    print("Lendo")
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='') # : Para ler linha por linha do arquivo
    print(arquivo.readline().strip()) 
    print(arquivo.readline().strip())
    print("READLINES")
    arquivo.seek(0, 0)
    for linha in arquivo.readlines(): # : Retorna uma lista com todas linhas do arquivo (também pega o '\n' junto)
        print(linha.strip()) # : strip() para tirar o espaços do começo e final ('\n' também conta como espaço)

print('=' * 40)
with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: # > Com with open, ele abre o arquivo e fecha sozinho no final
    print(arquivo.read())

# os.remove(caminho_arquivo) # > Apaga o arquivo, os.unlink() também funciona para remover
# os.rename(caminho_arquivo, 'arquivo_renomeado.txt') # > Para renomear arquivo, ou mudar de caminho, o nome tem que conter o caminho do arquivo
