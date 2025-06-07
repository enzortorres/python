class Animal:
    # nome = 'Leão'
    
    def __init__(self, nome):
        self.nome = nome
        
        variavel = 'valor'
        print(variavel)
    
    def acao(self):
        return f'{self.nome} está executando uma ação'
    
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
        
leao = Animal('Leão')

print(leao.nome)
print(leao.acao())
print(leao.comendo('maçã'))
print(leao.executar('banana'))