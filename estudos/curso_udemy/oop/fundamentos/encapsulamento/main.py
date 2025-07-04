"""
    | Encapsulamento (modificadores de acesso: public, protected, private)
    ? Python NÃO TEM modificadores de acesso
    ? Mas podemos seguir as seguintes convenções
        > (sem underline) = public
        : pode ser usado em qualquer lugar.
        
        > _ (um underline) = protected
        : não DEVE ser usado fora da classe ou suas subclasses.
        
        > __ (dois underlines) = private
        : "name mangling" (desfiguração de nomes) em Python só deve ser usado na classe em que foi declarado.
"""
class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'
        
    def metodo_public(self):
        # print(self.__private)
        # print(self.__metodo_private())
        return 'método public'
    
    def _metodo_protected(self):
        return 'método protected'
    
    def __metodo_private(self):
        return 'método privado'

f = Foo()
print(f.public)
print(f._protected)
# print(f.__private) # ! ERRO DE HERANÇA

print(f.metodo_public())
print(f._metodo_protected())
# print(f.__metodo_private()) # ! ERRO DE HERANÇA
print('name mangling:', f._Foo__metodo_private()) # > name mangling