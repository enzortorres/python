"""
    | @property - um getter no modo Pythônico
    ? getter - um método para obter um atributo
    
    * cor -> get_cor()
    
    ? modo pythônico - modo do Python de fazer coisas
    ? @property é uma propriedade do objeto, ela é um método que se comporta como um atributo
    
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
        self.cor_tinta = cor

    @property
    def cor(self):
        print("PROPERTY")
        return self.cor_tinta

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
