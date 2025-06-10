# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2025
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome': 'EnzoDict', 'idade': 25}

p1 = Pessoa('Enzo', 20)
p2 = Pessoa(**dados)
# p1.nome = 'Teste'
# print(p1.nome)
# print(p1.get_ano_nascimento())

# p1.__dict__['outra'] = 'Teste' # ? element.__dict__ é modificavel
# print(p1.__dict__)
# print(vars(p1))
# del p1.__dict__['nome']

print(p1.__dict__)

print(p2.__dict__)