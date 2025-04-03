def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func): # > Decoradores recebem uma função como parâmetro obrigatoriamente
        print('Decoradora 1')
        
        def aninhada(*args, **kwargs):
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


lista = []
def soma(x, y):
    return x + y

decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)
