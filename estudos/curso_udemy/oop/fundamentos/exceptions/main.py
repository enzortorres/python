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

class MyError(Exception):
    ...
    
class AnotherError(Exception):
    ...
    
def levantar():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Você errou isso')
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = AnotherError('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    
    raise exception_ from error