"""
    | __new__ e __init__ em classes Python
    ? __new__ é o método responsável por criar e retornar o novo objeto. Por isso, new recebe cls
    ! __new__ DEVE retornar o novo objeto 
    
    ? __init__ é o método responsável por inicializar a instância. Por isso, init recebe self.
    ! __init__ NÃO DEVE retornar nada (None)
    
    ? Object é a super classe de uma classe
"""
class A:
    def __new__(cls, *args, **kwargs): # para usar atributos no init, precisa colocar no new também (args e kwargs resolvem)
        print('Antes de criar a instância')
        instancia = super().__new__(cls)
        print('Depois de criar a instância')
        instancia.x = 213 # bom para quando um atributo obrigatoriamente precisa ser esse valor
        return instancia
    
    def __init__(self, y):
        print('Sou o init')
        self.y = y
    
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(y={self.y})'
    
a = A(10)
print(a)
print(a.y)