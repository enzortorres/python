"""
    | @property + @setter - getter e setter no modo Pythônico
    ? getter - um método para obter um atributo
    
    * cor -> get_cor()
    
    ? modo pythônico - modo do Python de fazer coisas
    ? @property é uma propriedade do objeto, ela é um método que se comporta como um atributo
    ? atributos que começar com um ou dois "_", não devem ser usados fora da classe.
    
    : Geralmente é usada nas seguintes situações:
        > como getter
        > para evitar quebrar código cliente
        > para habilitar setter
        > para executar açõoes ao obter um atributo
    
    ? Código cliente - é o código que usa o seu código
"""

# class Caneta:
#     def __init__(self, cor):
#         # private, protected, public
#         self.cor = cor
    
#     def get_cor(self):
#         print('GET COR')
#         return self.cor

# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property # getter
    def cor(self):
        return self._cor
    
    @cor.setter # setter, é bom criar o setter assim para poder criar restrições
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError("Não aceito essa cor")
        
        self._cor = valor
    
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
caneta.cor_tampa = 'Azul'

caneta.cor = 'Pink'

print('Cor: ', caneta.cor)
print('Cor tampa: ', caneta.cor_tampa)

# caneta.cor = 'Vermelho' # ! ERRO
# ? caneta.cor deixou de ser um atributo e passou a ser um getter com @property
