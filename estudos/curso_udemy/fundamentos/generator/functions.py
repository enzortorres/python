# # ! Introdução às Generator functions em Python

def generator(n=0):
    yield 1 # > Pausar
    print('Continuando...') # > Quando chama o segundo next ele executa o restante do código
    yield 2 # > Pausar
    print('Mais uma...') # > Quando chama o segundo next ele executa o restante do código
    yield 3 # > Pausar
    print('Vou terminar')
    return 'ACABOU'

# gen = generator(n=0)
# print(next(gen)) # : 1 (Primeiro yield)
# print(next(gen)) # : Continuando... 2 (Restante do código, pausando no segundo yield)
# print(next(gen)) # : Mais uma... (Restante do código, pausando no terceiro yield)
# print(next(gen)) # : Vou terminar, finalizou a generator function, StopIteration: ACABOU

def generator(n=0, maximum = 10):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return

gen = generator()
for n in gen:
    print(n)

# ? Yield from

def gen1():
    print('COMEÇOU GEN1')
    yield 1
    yield 2
    yield 3
    print('TERMINOU GEN1')
    

def gen2(gen=None):    
    print('COMEÇOU GEN2')
    if gen is not None:
        yield from gen()
    yield 4
    yield 5
    yield 6
    print('TERMINOU GEN2')

def gen3():
    print('COMEÇOU GEN3')
    yield 10
    yield 20
    yield 30
    print('TERMINOU GEN3')
    

g1 = gen2(gen1)
g2 = gen2(gen3)
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)