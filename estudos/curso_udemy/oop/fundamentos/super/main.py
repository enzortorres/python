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
    atributo_b = 'valor B'
    
    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor C'
    
    def metodo(self):
        print('C')


a = A()
b = B()
c = C()

print(a.atributo_a)
print(b.atributo_a)
print(b.atributo_b)
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
a.metodo()
b.metodo()
c.metodo()