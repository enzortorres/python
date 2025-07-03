"""
    | Métodos de classe + factories (fábricas)
    ? São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, receberemos a própria classe.
"""

class Pessoa:
    ano = 2025 # atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls("Anônima", idade)

p1 = Pessoa('João', 35)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome('30')
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)


p1.metodo_de_classe()
Pessoa.metodo_de_classe()


class Connection:
    def __init__(self, host = 'localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user): # sempre que precisar de self dentro do método, é um método de instância
        self.user = user
        
    def set_passwd(self, password):
        self.password = password
        
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        
        return connection

c1 = Connection.create_with_auth('username', '1234')
# c1.set_user('username')
# c1.set_passwd('123')
print(c1.user)
print(c1.password)