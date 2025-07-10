"""
    | Herança simples - Relações entre classes
    > Associação - usa outro objeto
    > Agregação - tem outro objeto
    
    > Composição - É dono de outro objeto
    > Herança - É um 
    
    ? Herança ou Composição
    
    > Classe principal (Veiculo), (Pessoa), (Produto)
        : super class, base class, parent class
    > Classes filhas (Carro), (Cliente), (Computador)
        : sub class, child class, derived class
    
    ex: Carro é um Veiculo
    ex: Cliente é uma Pessoa
    ex: Computador é um Produto
"""

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print()
        print('Original da pessoa')
        print('Pessoa:',self.nome, self.sobrenome ,self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_classe(self):
        super().falar_nome_classe()
        print('Cliente')
    
class Aluno(Pessoa):
    def falar_nome_classe(self):
        super().falar_nome_classe()
        print('Aluno')

p1 = Pessoa('Marcos', 'Castro')
p1.falar_nome_classe()

c1 = Cliente('Enzo', 'Ribas')
c1.falar_nome_classe()

a1 = Aluno('João', 'Carlos')
a1.falar_nome_classe()
