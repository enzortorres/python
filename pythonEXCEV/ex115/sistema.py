from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

try:
    arq = 'lista.txt'
except KeyboardInterrupt:
    print('Usuário interrompeu o sistema.')
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('          \033[4;31mNOVO CADASTRO\033[m')
        nome = str(input('\033[35mNome: '))
        idade = leiaInt('Idade: \033[m')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('      \033[35mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)
