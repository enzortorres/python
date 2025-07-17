"""
    | Criando Exceptions - Python Orientado a Objetos
    ? Para criar um Exception em Python, você só precisa herdar de alguma exceção da linguagem.
    ? A recomendação da doc é herdar de Exception.
    > https://docs.python.org/pt-br/3.13/library/exceptions.html
    
    ? Criando exceções (comum colocar Error no final)
    ? Levantando (raise) / lançando (throw) exceções
    ? relançando exceções
    ? Adicionando notas em exceções (3.11.0)
"""

class MyErro(Exception):
    ...
    
def levantar():
    raise MyErro('A mensagem do meu erro')

levantar()