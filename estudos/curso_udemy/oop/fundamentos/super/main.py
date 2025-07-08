"""
    | super() é a super classe na sub classe
    
    : Classe principal (Veiculo)
        > super class, base class, parent class
    : Classe filhas (Carro)
        > sub class, child class, derived class
"""

class MinhaString(str):
    def upper(self):
        # return 'ABC'
        print('CHAMOU UPPER')
        retorno = super().upper()
        print('DEPOIS DO UPPER')
        return retorno

string = MinhaString('Enzo')
print(string)
print(string.upper())

class A:
    atributo_a = 'valor A'
    
    def metodo(self):
        print('A')

class B(A):
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
    
    atributo_b = 'valor B'
    
    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor C'
    
    def __init__(self, *args, **kwargs):
        print('EI, burlei o sistema')
        super().__init__(*args, **kwargs)
    
    def metodo(self):
        super(C, self).metodo() # padrão
        # self().metodo() # mesma coisa ^
        # super(B, self).metodo() # ? começar a procurar pelo super da classe B (A)
        print('C')


# a = A()
# b = B()
# c = C()

# print(a.atributo_a)
# print(b.atributo_a)
# print(b.atributo_b)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# a.metodo()
# b.metodo()
# c.metodo()

print(C.mro())