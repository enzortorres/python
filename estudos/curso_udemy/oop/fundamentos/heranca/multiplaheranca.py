"""
    | Herança Múltipla - Python Orientado a Objetos
    ? Quer dizer que no Python, uma classe pode estender várias outras classes.
    
    > Herança simples:
        : Animal -> Mamifero -> Humano -> Pessoa -> Cliente
        ex: Cliente(Pessoa)

    > Herança múltipla e mixins
        : Log -> FileLog
        : Animal -> Mamifero -> Humano -> Pessoa -> Cliente
        ex: Cliente(Pessoa, FileLog)
    
    ex: A, B, C, D
    ex: D(B, C) - C(a) - B(A) - A
    
    ex:
        >         A
        >       /   \
        >      B     C
        >       \   /
        >         D
    
    ? Python 3 usa C3 superclass linearization para gerar o mro.
    ? Não precisa estudar isso (é complexo)
    > https://www.geeksforgeeks.org/python/c3-linearization-algorithm-in-python/
    
    ? Para saber a ordem de chamada dos métodos use o método de classe Classe.mro()
    ? Ou o atributo __mro__ (Dunder - Double Underscore)
"""
class A:
    ...
    
    def quem_sou(self):
        print('A')
class B(A):
    ...
    
    def quem_sou(self):
        print('B')
class C(A):
    ...
    
    def quem_sou(self):
        print('C')
class D(B, C): # ? A primeira classe a ser herdada tem prioridade no mro
    ...
    
    def quem_sou(self):
        print('D')

d = D()
d.quem_sou()
# print(D.mro()) 