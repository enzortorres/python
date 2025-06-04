"""
    | class - Classes são moldes para criar novos objetos.
    ? As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
    ? Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
    ? Por convenção, usamos PascalCase para nomes de classes ( ExemploDeVariavel )
"""

# string = 'Enzo' # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Enzo', 'Ribas') # gera uma nova instância da classe pessoa para a variavél p1
# p1.nome = 'Enzo'
# p1.sobrenome = 'Ribas'

p2 = Pessoa('Maria', 'Joana') # gera uma nova instância da classe pessoa para a variavél p2
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)
