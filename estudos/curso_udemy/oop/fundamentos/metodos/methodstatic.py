"""
    | @staticmethod (métodos estáticos) são inúteis em Pyhon =)
    ? Métodos estáticos são métodos que estão dentro da classe, mas não tem acesso ao self nem ao cls.
    ? Em resumo, são funções que existem dentor da sua classe.
"""

class Classe:
    
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)

c1 = Classe()
c1.funcao_que_esta_na_classe(1,2,3)
Classe.funcao_que_esta_na_classe(nomeado=1)

print("\n" * 3)

class Connection:
    def __init__(self, host='localhost'):  # sempre que precisar de self dentro do método, é um método de instância
        self.host = host
        self.user = None
        self.password = None
    
    @staticmethod
    def soma(x, y):
        return x + y
    
    @staticmethod
    def log(msg):
        print('LOG:', msg)

print(Connection.soma(5, 2))
Connection.log('Essa é uma mensagem do log')